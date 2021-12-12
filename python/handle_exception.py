import asyncio
import sys


def handle_exception(exc_type, exc_value, exc_traceback):
    print(f"2: {exc_value!r}")


sys.excepthook = handle_exception
from asyncio import sleep


async def f():
    await sleep(1.1)
    1 / 0


async def main():
    try:
        asyncio.create_task(f())
        await asyncio.sleep(0.1)
    except Exception as e:
        print(f"2: {e!r}")


if __name__ == "__main__":
    asyncio.run(main())
