from esmerald import get


@get()
async def welcome_from_add_route() -> dict:
    return {"message": "Hello again, let's use 'add_route', too!"}
