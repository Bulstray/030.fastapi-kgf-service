from fastapi import APIRouter, Request

from fastapi.responses import HTMLResponse

from templating.jinja_template import templates

router = APIRouter()


@router.get("/")
async def programs_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        name="programs.html",
        request=request,
    )
