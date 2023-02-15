from esmerald import Esmerald, get, Gateway, Include

from endpoints.add_route_resource import welcome_from_add_route
from endpoints.childesmerald_resource import child_esmerald
from endpoints.more_resource import my_urls
from endpoints.router_resource import my_router


@get()
async def homepage() -> dict:
    return {"message": "Hello world!"}


@get()
async def introduction() -> dict:
    return {"message": "I am an Esmerald API!"}


esmerald_app = Esmerald(
    routes=[
        Gateway(path="/", handler=homepage),
        Include(path="/include", routes=my_urls),
        Include(path="/include", namespace="endpoints.even_more_resource"),
        Include(path="/childesmerald", app=child_esmerald),
    ]
)

esmerald_app.router.add_route(path="/add_route", handler=introduction)
esmerald_app.add_route(path="/add_route2", handler=welcome_from_add_route)
esmerald_app.add_router(router=my_router)
