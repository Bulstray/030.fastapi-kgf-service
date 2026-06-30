from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from templating.jinja_template import templates

router = APIRouter()


@router.get("/", name="login:get")
async def login_page(
    request: Request,
) -> HTMLResponse:
    return templates.TemplateResponse(
        name="login.html",
        request=request,
    )
