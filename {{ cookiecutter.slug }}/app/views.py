import aiohttp_jinja2
from aiohttp import web


async def root_view(request):
    return aiohttp_jinja2.render_template("index.html", request, {})


async def dynamic_view(request):
    page = request.match_info["page"]

    # safety check
    if not page.replace("-", "").replace("_", "").isalnum():
        raise web.HTTPNotFound()

    template_name = f"{page}.html"

    return aiohttp_jinja2.render_template(template_name, request, {})
