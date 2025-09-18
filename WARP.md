# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

CodeExamples is a collection of Python scripts demonstrating various programming concepts, performance optimizations, and practical implementations. The codebase serves as a learning resource and reference for Python development patterns.

## Architecture

### Code Organization
All example scripts are located in the `code/` directory with a flat structure. Examples fall into these categories:

- **Performance Comparisons**: Files comparing different approaches or libraries (e.g., `orjson_vs_json.py`, `numpy_vs_numexpr.py`, `list_comp_vs_manual.py`)
- **Algorithm Implementations**: Data structures and algorithms (e.g., `BloomFilter.py`, `Kth_largest_element.py`, `merge_intervals.py`)
- **Web Framework Examples**: FastAPI, async programming, and HTTP client examples
- **Database Integration**: MongoDB, OpenAI embeddings, and data processing examples
- **System Programming**: Context managers, threading, Cython extensions
- **External API Integration**: Web scraping, authentication, and third-party service examples

### Cython Extensions
The repository includes Cython performance examples:
- `cyton_fast_sum.pyx`: Cython implementation for high-performance array summation
- `cyton_fast_sum.c`: Generated C code from Cython compilation
- `cyton_fast_sum.cp313-win_amd64.pyd`: Compiled extension for Python 3.13 on Windows

## Development Environment

### Python Version
The project uses Python 3.13 as specified in `.python-version`.

### Environment Setup
Since this is a collection of standalone examples, most scripts can be run independently. Some examples may require specific packages:

```powershell
# For performance comparison examples
pip install orjson numexpr numpy

# For web examples
pip install fastapi uvicorn starlette

# For database examples
pip install pymongo requests

# For specific examples
pip install pyseto babel cython pydantic patterns
```

## Running Examples

### Standard Python Scripts
Most examples can be run directly:

```powershell
python code/BloomFilter.py
python code/async_threads.py
python code/orjson_vs_json.py
```

### FastAPI Applications
For web service examples:

```powershell
# Run FastAPI applications with uvicorn
python code/async_threads.py  # Includes built-in uvicorn.run()
python code/fastapi_dependency_injection.py
```

### HTTP Request Testing
Some examples include `.http` files for testing HTTP endpoints:
- Use REST Client extension in VS Code or similar tools to execute requests in `async_threads.http`

### Cython Extensions
To rebuild Cython extensions:

```powershell
# Install development dependencies
pip install cython

# Build extension (if setup.py exists)
python setup.py build_ext --inplace

# Or manually compile
cython -3 code/cyton_fast_sum.pyx
```

### Performance Benchmarks
Performance comparison scripts typically output timing results directly:

```powershell
python code/numpy_vs_numexpr.py
# Output: NumPy time: X.XXXX seconds
#         NumExpr time: X.XXXX seconds
#         NumExpr is faster than NumPy in X.X times
```

## Code Patterns

### Performance Measurement
Examples consistently use `timeit` module for benchmarking:

```python
import timeit
time_taken = timeit.timeit(lambda: function_to_test(), number=iterations)
```

### Error Handling
Examples include practical error handling patterns, especially for external API calls:

```python
try:
    response.raise_for_status()
    # Process response
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

### Context Managers
Several examples demonstrate custom context manager patterns:
- Rate limiting (`context_manager_throttle_rate.py`)
- Thread synchronization (`context_manager_lock_thread.py`)
- Resource management (`context_manager_stack.py`)

## Testing Individual Scripts

To run a single example script in window mode (as per user preference):

```powershell
python -i code/script_name.py  # Interactive mode to see output
```

Or simply:

```powershell
python code/script_name.py
```

The repository does not include a traditional test suite since these are demonstration scripts rather than production code.

## Key Files to Understand

- `pyproject.toml`: Basic project configuration with Python 3.13 requirement
- `code/patterns_usage.py`: Demonstrates design patterns using the `patterns` library
- `code/openai_embeddings.py`: Shows OpenAI API integration and MongoDB vector search
- `code/fastapi_dependency_injection.py`: Protocol-based dependency injection pattern
- `code/BloomFilter.py`: Complete implementation of probabilistic data structure

## Notes for Development

- Scripts are self-contained demonstrations - avoid adding complex dependencies
- Performance comparisons should include clear output showing relative improvements  
- When adding new examples, follow the existing naming convention (snake_case)
- Include docstrings explaining the concept being demonstrated
- For examples requiring external services, include error handling for connection failures