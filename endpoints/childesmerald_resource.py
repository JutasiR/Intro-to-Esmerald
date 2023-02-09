from esmerald import ChildEsmerald, get, Gateway


@get(path="/hello")
async def hello_from_childesmerald() -> dict:
    return {"message": "Hello World from the child esmerald!"}


child_esmerald = ChildEsmerald(
    routes=[Gateway(handler=hello_from_childesmerald)],
)
