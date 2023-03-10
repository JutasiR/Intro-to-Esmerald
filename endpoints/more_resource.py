from esmerald import get, Gateway


@get()
async def another_home() -> dict:
    return {"message": "Hello again, world!"}


my_urls = [Gateway(path="/route_list", handler=another_home)]
