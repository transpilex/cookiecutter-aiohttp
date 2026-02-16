import jinja2
import aiohttp_jinja2
from aiohttp import web

from .config import settings
from .routes import setup_routes


def create_app():
    app = web.Application()

    app["settings"] = settings

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(settings.TEMPLATES_DIR)))

    app.router.add_static(settings.STATIC_URL, path=str(settings.STATIC_DIR), name="static")

    setup_routes(app)

    return app
