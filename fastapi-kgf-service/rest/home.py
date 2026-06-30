from fastapi import APIRouter, Request

from templating.jinja_template import templates

router = APIRouter()


@router.get("/")
async def home_page(request: Request):
    return templates.TemplateResponse(
        name="home.html",
        request=request,
    )
