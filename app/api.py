from fastapi import APIRouter, Request, HTTPException, status

from app.config import fake_data_map
from app.utils import generate_fake_data

api = APIRouter(prefix="/api")


@api.post("/")
async def generate_data(req: Request):
    formdata = await req.json()
    if len(formdata) < 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="json body required",
        )
    return generate_fake_data(formdata)


@api.get("/types")
async def get_datatypes():
    res = [i for i in fake_data_map.keys()]
    return res