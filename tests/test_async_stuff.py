from asyncio import sleep


async def test_sleep(): 
    await sleep(0.2)
    raise Exception("boo")