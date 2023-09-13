"""NOTES:
1.
If your application (somehow) doesn't have to communicate with anything else and wait for it to respond, use async def.

 """

async def get_burgers(number: int) -> int:
    return number

async def read_burgers():
    burgers = await get_burgers(3)
    return burgers