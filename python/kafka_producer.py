import json
import os

from aiokafka import AIOKafkaProducer
import asyncio

from dotenv import load_dotenv

config = load_dotenv()  # take environment variables from .env.


async def send_one():
    producer = AIOKafkaProducer(
        bootstrap_servers=os.getenv("BOOTSTRAP_SERVERS"))
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        msg = {}
        msg = json.dumps(msg).encode()
        await producer.send_and_wait(os.getenv("TOPIC"), msg)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()


if __name__ == "__main__":

    asyncio.run(send_one())