"""
Pool everything: HTTP clients, DB, cache
Goal: downstream calls add <10 ms median and never explode p99.

Why it helps: new TCP/TLS handshakes and cold DB sockets are silent p99 killers.
"""

"""
Reuse sockets with httpx and set sharp timeouts:
"""
import httpx

client = httpx.AsyncClient(
    http2=True,
    limits=httpx.Limits(max_connections=1000, max_keepalive_connections=200),
    timeout=httpx.Timeout(connect=0.2, read=0.3, write=0.3, pool=0.2)
)

"""
Size DB pools explicitly (example asyncpg):
"""
import asyncpg

async def pg_pool(DSN: str) -> asyncpg.Pool:
    pool = await asyncpg.create_pool( dsn=DSN, min_size=5, max_size=50, command_timeout=0.3)
    return pool
