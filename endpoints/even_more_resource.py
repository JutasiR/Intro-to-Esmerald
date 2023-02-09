from esmerald import get, Gateway


@get()
async def yet_another_home() -> dict:
    return {"message": "Hello my dear old friend, world!"}


route_patterns = [Gateway(handler=yet_another_home)]
