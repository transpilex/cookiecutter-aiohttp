from aiohttp import web
from app.main import create_app
from app.config import settings

if __name__ == "__main__":
    app = create_app()
    web.run_app(app, host=settings.HOST, port=settings.PORT)
