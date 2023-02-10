from esmerald import Esmerald, get, Gateway, Include
from endpoints.childesmerald_resource import child_esmerald
from endpoints.more_resource import my_urls


@get()
async def homepage() -> dict:
    return {"message": "Hello world!"}


esmerald_app = Esmerald(
    routes=[
        Gateway(path="/", handler=homepage),
        Include(path="/route_list", routes=my_urls),  # using route list
        Include(
            path="/namespace", namespace="endpoints.even_more_resource"
        ),  # using namespace with default
        Include(path="/childesmerald", app=child_esmerald),
    ]
)
