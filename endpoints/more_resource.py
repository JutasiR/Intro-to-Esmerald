from esmerald import get, Gateway


@get()
async def another_home() -> dict:
    return {"message": "Hello again, world!"}


my_urls = [Gateway(handler=another_home)]
