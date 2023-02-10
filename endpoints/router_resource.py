from esmerald import get, Router, Gateway


@get()
async def home_for_router() -> dict:
    return {"message": "Hello from a router, world!"}


my_router = Router(path="/router", routes=[Gateway(handler=home_for_router)])
