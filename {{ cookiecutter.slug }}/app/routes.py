from .views import root_view, dynamic_view


def setup_routes(app):
    app.router.add_get("/", root_view)
    app.router.add_get(r"/{page:[a-zA-Z0-9_-]+}", dynamic_view)
