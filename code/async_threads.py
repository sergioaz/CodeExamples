import time
from fastapi import FastAPI, Depends, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import asyncio
from concurrent.futures import ThreadPoolExecutor

app = FastAPI(
    title="Async testing",
    description="API for searching addresses using Elasticsearch with comparison capabilities",
    version="1.0.0",
    #lifespan=lifespan
)


async def long_running_cpu_task():
    total = sum(i * i for i in range(10_000_000))
    return {"total": total}


class MeasureTime(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response: Response = await call_next(request)
        duration = time.time() - start
        response.body["duration"] = duration

        return response


from fastapi import FastAPI

app = FastAPI()
app.add_middleware(MeasureTime)

@app.get("/no_thread")
async def no_thread():
    result = await long_running_cpu_task()
    return {"data": result}


executor = ThreadPoolExecutor()
@app.get("/yes_thread")
async def yes_thread():
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, long_running_cpu_task)
    return {"result": result}

def main():
    import uvicorn
    uvicorn.run(
        "athinc_threads:app",
        host="localhost",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()