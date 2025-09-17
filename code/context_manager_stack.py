"""
Pro Tip: Stack Context Managers Cleanly
You can stack multiple managers like this:
with Timer("Job"), suppress_stdout(), throttle(0.5):
    run_job()

Or use contextlib.ExitStack() when you don’t know how many you’ll need:
"""
from contextlib import ExitStack

with ExitStack() as stack:
    for res in resources:
        stack.enter_context(open(res))
    # Now all files are open and auto-closed after

