# CodeExamples 🐍

A curated collection of Python code examples demonstrating practical programming concepts, performance optimizations, and real-world implementations. Perfect for developers looking to learn new techniques, compare approaches, or find reference implementations.

## 🌟 What's Inside

This repository contains **40+ Python examples** covering:

- **Performance Comparisons** - See how different libraries and approaches stack up
- **Algorithm Implementations** - Classic data structures and algorithms
- **Web Development** - FastAPI, async programming, and HTTP patterns
- **Database Integration** - MongoDB, embeddings, and data processing
- **Advanced Python** - Context managers, generators, decorators, and more
- **External APIs** - Authentication, web scraping, and service integration

## 🚀 Getting Started

### Prerequisites
- Python 3.13 (specified in `.python-version`)
- Individual examples may require specific packages (install as needed)

### Quick Start
```bash
# Clone and explore
git clone <repository-url>
cd CodeExamples

# Run any example directly
python code/BloomFilter.py
python code/merge_intervals.py
python code/orjson_vs_json.py
```

## 📚 Featured Examples

### 🔧 Smart Context Managers
Perfect your resource management and API rate limiting:

```python
# From context_manager_throttle_rate.py
from contextlib import contextmanager
import time

@contextmanager
def throttle(seconds):
    yield
    time.sleep(seconds)

# Usage: Never get rate-limited again!
for _ in range(5):
    with throttle(1):  # Pause 1 second between calls
        ping_api()
```

### 🎯 Elegant Algorithm Implementation
Clean, efficient interval merging:

```python
# From merge_intervals.py
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example: [[15,18], [8,10], [1,3], [2,6]] → [[1,6], [8,10], [15,18]]
```

### 🔍 Memory-Efficient File Processing
Handle massive files without breaking a sweat:

```python
# From iterator_generator.py
def take_n(n, itr):
    result = []
    for i in range(n):
        try:
            result.append(next(itr))
        except StopIteration:
            break
    return result

# Process huge files efficiently
with open('my_huge_file.txt', 'r') as FILE:
    results = take_n(3, filter(find_my_pattern, 
                              (line for line in FILE)))
```

### 🛡️ Secure Password Handling
Production-ready password hashing with salt:

```python
# From password_hash.py
import hashlib, os

password = "mypassword123"
salt = os.urandom(16)

# Strong password hashing
hashed = hashlib.pbkdf2_hmac(
    'sha256',                  # Hash algorithm
    password.encode('utf-8'),  # Convert to bytes
    salt,                      # Random salt
    100_000                    # Iterations (security)
)
```

### 🎨 Clean Enum Patterns
Make your code more readable and maintainable:

```python
# From enums_examples.py
from enum import Enum

class UserRole(Enum):
    ADMIN = 1
    EDITOR = 2
    VIEWER = 3
    
    def can_edit(self):
        return self in {UserRole.ADMIN, UserRole.EDITOR}
    
    def can_delete(self):
        return self == UserRole.ADMIN

# Clean usage
if user_role.can_edit():
    print("User can edit content")
```

### ⚡ Performance Showdowns
Real benchmarks with actual numbers:

```python
# From orjson_vs_json.py
import json, orjson, time

data = [{"id": i, "value": f"value-{i}"} for i in range(1_000_000)]

# Standard json
start = time.time()
json.dumps(data)
json_time = time.time() - start

# orjson
start = time.time()
orjson.dumps(data)
orjson_time = time.time() - start

print(f"orjson is {json_time/orjson_time:.2f}x faster!")
# Typical result: orjson is 2-3x faster!
```

### 🧮 Probabilistic Data Structures
Space-efficient membership testing:

```python
# From BloomFilter.py
class BloomFilter:
    def __init__(self, n_items, fp_rate=0.01):
        self.m = -int(n_items * math.log(fp_rate) / (math.log(2)**2))
        self.k = max(1, int((self.m / n_items) * math.log(2)))
        self.bitarr = bytearray((self.m + 7) // 8)
    
    def add(self, item):
        for pos in self._hashes(item):
            self.bitarr[pos // 8] |= 1 << (pos % 8)
    
    def __contains__(self, item):
        return all(self.bitarr[pos // 8] & (1 << (pos % 8)) 
                  for pos in self._hashes(item))

# Test millions of items with tiny memory footprint!
```

### 🔥 Cython Performance
When Python isn't fast enough:

```python
# From cyton_fast_sum.pyx
def fast_sum(long long[:] arr):
    cdef long long total = 0
    for i in range(arr.shape[0]):
        total += arr[i]
    return total

# Benchmark shows 10-50x speedup over pure Python!
```

## 🗂️ Example Categories

### 🏎️ Performance & Optimization
- `orjson_vs_json.py` - JSON serialization benchmarks
- `numpy_vs_numexpr.py` - Numerical computation comparisons  
- `list_comp_vs_manual.py` - List comprehension vs traditional loops
- `cyton_example.py` - Cython performance testing
- `profile_function.py` - Code profiling techniques

### 🧮 Data Structures & Algorithms
- `BloomFilter.py` - Probabilistic data structure implementation
- `Kth_largest_element.py` - Efficient selection algorithm
- `merge_intervals.py` - Interval merging algorithm
- `get_duplicates.py` - Duplicate detection using Counter
- `prime_numbers.py` - Prime number generation

### 🌐 Web Development
- `fastapi_dependency_injection.py` - Clean DI patterns
- `fastapi_htmx.py` - Modern web interfaces
- `async_threads.py` - Concurrent request handling
- `capture_headers.py` - HTTP header processing

### 🔧 Python Patterns & Best Practices  
- `context_manager_*.py` - Custom context managers
- `iterator_generator.py` - Memory-efficient file processing
- `enums_examples.py` - Clean enum usage
- `patterns_usage.py` - Design pattern implementations
- `logging_with_extra_parameter.py` - Advanced logging

### 🛡️ Security & Authentication
- `password_hash.py` - Secure password handling
- `auth_by_pyseto.py` - Modern token authentication

### 🗄️ Database & APIs
- `openai_embeddings.py` - Vector search with MongoDB
- `mongo_shard.py` - MongoDB operations
- `get_youtube_transcript.py` - API integration

## 🎯 Learning Paths

### **Beginner Path** 🟢
Start with these fundamental examples:
1. `merge_intervals.py` - Learn algorithm thinking
2. `get_duplicates.py` - Understand data processing
3. `enums_examples.py` - Clean code patterns
4. `iterator_generator.py` - Memory efficiency

### **Intermediate Path** 🟡  
Level up with these examples:
1. `context_manager_throttle_rate.py` - Advanced Python features
2. `fastapi_dependency_injection.py` - Web development patterns
3. `BloomFilter.py` - Data structure implementation
4. `password_hash.py` - Security practices

### **Advanced Path** 🔴
Master these complex topics:
1. `async_threads.py` - Concurrent programming
2. `cyton_example.py` - Performance optimization
3. `openai_embeddings.py` - AI/ML integration
4. `patterns_usage.py` - Design patterns

## 🏃‍♂️ How to Run Examples

### Single Scripts
```bash
python code/BloomFilter.py
python code/merge_intervals.py
python code/orjson_vs_json.py
```

### Web Applications
```bash
# FastAPI applications include uvicorn.run()
python code/async_threads.py
python code/fastapi_dependency_injection.py

# Then visit http://localhost:8000
```

### Performance Benchmarks
```bash
# These show timing comparisons
python code/numpy_vs_numexpr.py
python code/list_comp_vs_manual.py
python code/orjson_vs_json.py
```

### Interactive Examples
```bash
# Some examples require input
python code/password_hash.py
python code/login_to_upwork.py
```

## 📦 Dependencies

Most examples are self-contained, but some may require:

```bash
# For performance examples
pip install orjson numexpr numpy

# For web examples  
pip install fastapi uvicorn starlette

# For database examples
pip install pymongo requests

# For specific examples
pip install pyseto babel cython pydantic patterns
```

## 🤝 Contributing

Found a bug? Have a cool example to add? Contributions welcome! 

- Keep examples focused and well-documented
- Include timing comparisons for performance examples
- Follow the existing naming conventions (snake_case)
- Add docstrings explaining the concept demonstrated

## 📖 More Resources

- Check `WARP.md` for development guidance
- Each example includes inline documentation
- Many examples include comparative analysis
- Look for related examples in similar categories

---

**Happy Coding!** 🎉 Explore, learn, and build amazing things with Python.

*"The best way to learn programming is by reading and writing code."* - Start exploring! 🚀