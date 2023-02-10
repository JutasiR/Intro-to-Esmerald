from esmerald import get, Gateway


@get()
async def yet_another_home() -> dict:
    return {"message": "Hello my dear old friend, world!"}


route_patterns = [Gateway(path="/namespace", handler=yet_another_home)]
