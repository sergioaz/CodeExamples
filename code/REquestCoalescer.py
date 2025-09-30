"""
Request coalescing (aka singleflight) groups concurrent requests for the same key so only one upstream call runs; other callers wait and get that single result. Useful when upstream is slow/expensive and many clients ask for the same missing key.
Explanation: the example below shows a simple synchronous coalescer using a per-key in-flight map with threading.Event. The first caller starts the fetch; others wait on the event and then receive the result or exception.

"""
import threading
import time
from typing import Any, Callable, Dict, Optional, Tuple

class RequestCoalescer:
    """
    Simple synchronous request coalescing.
    - fetch_fn: callable(key) -> value (may raise)
    - cache optional to short-circuit hits
    """
    def __init__(self, fetch_fn: Callable[[str], Any]):
        self.fetch_fn = fetch_fn
        self._inflight: Dict[str, Tuple[threading.Event, Optional[Any], Optional[BaseException]]] = {}
        self._lock = threading.Lock()
        self._cache: Dict[str, Any] = {}

    def get(self, key: str) -> Any:
        # Fast path: cached value
        if key in self._cache:
            return self._cache[key]

        with self._lock:
            # If another thread is already fetching, wait for it
            if key in self._inflight:
                event, result, exc = self._inflight[key]
                # Release lock then wait
            else:
                # Register ourselves as the fetcher
                event = threading.Event()
                self._inflight[key] = (event, None, None)
                # Mark that we will fetch (other threads will wait)
                is_fetcher = True
                # release lock and fetch below
                # store local reference for cleanup
                fetch_event = event
                # fetch outside lock
                break_fetch = False
                # use sentinel to indicate we will fetch
                # (we'll use a simple control flow)
                pass

        # If we found an existing inflight, wait until event is set
        if key in self._inflight and not ('is_fetcher' in locals()):
            event, result, exc = self._inflight[key]
            event.wait()
            # after wait, read result/exception set by fetcher
            _, result, exc = self._inflight.get(key, (None, None, None))
            if exc:
                raise exc
            return result

        # The thread that reaches here is the fetcher
        try:
            value = self.fetch_fn(key)
            # store in cache (optional)
            self._cache[key] = value
            with self._lock:
                # update inflight with result
                event, _, _ = self._inflight.get(key, (None, None, None))
                if event:
                    self._inflight[key] = (event, value, None)
                    event.set()
            return value
        except BaseException as e:
            with self._lock:
                event, _, _ = self._inflight.get(key, (None, None, None))
                if event:
                    self._inflight[key] = (event, None, e)
                    event.set()
            raise
        finally:
            # cleanup inflight entry after notifying waiters
            with self._lock:
                self._inflight.pop(key, None)


# --- Example usage --- #

def slow_upstream(key: str) -> str:
    time.sleep(1)  # simulate slow call
    return f"value-for-{key}"


def worker(key: str):
    print(f"Requesting: {key}")
    val = coalescer.get(key)
    print("Got", val)

if __name__ == "__main__":
    coalescer = RequestCoalescer(slow_upstream)
    threads = [threading.Thread(target=worker, args=("k1",)) for _ in range(4)]
    for t in threads: t.start()
    for t in threads: t.join()
