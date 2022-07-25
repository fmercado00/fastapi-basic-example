# Python
from enum import Enum
from importlib.resources import path
import os
from tempfile import NamedTemporaryFile
from typing import Optional


# Models
from models.city import City
from models.person_base import PersonBase
from models.requests.person_request_model import PersonRequestModel
from models.response.person_response_model import PersonResponseModel
from models.response.login_response_model import LoginResponseModel
from models.location import Location

# Pydantic
from pydantic import BaseModel, Field, validator

#FastApi
from fastapi import FastAPI, Body, Query, Path, status, Header, Form, File, UploadFile, Depends, HTTPException, Cookie

app = FastAPI()

@app.get(
    path="/", 
    status_code=status.HTTP_200_OK,
    tags=["Ping"],
    )

def root(status_code=status.HTTP_200_OK):
    return {"message": "Endpoint for the person API"}

# Reques and response body
@app.post(
    path="/person/new",
    response_model=PersonResponseModel,
    status_code=status.HTTP_201_CREATED,
    tags=["Persons"],
    )
def create_person(person: PersonRequestModel = Body(...)):
    return person

# Validation : Query parameters
@app.get(
    path="/person/details/",
    status_code=status.HTTP_200_OK,
    tags=["Persons"],
    )
async def show_person(
    name: Optional[str] = Query(
        ..., 
        min_length=3,
        max_length=50,
        title="Person Name",
        description="This is the Person Name field. It's between 1 and 50 characters long.",
        example="John Doe",
        ),
    age: int = Query(
        ...,
        gt=18,
        lt=10.5,
        title="Person age",
        description="This is the Person age field. It's required.",
        example=20,
        )
    ): 
    return {"name": name, "age": age}

# Validation : Path parameters
@app.get(
    path="/person/details/{person_id}",
    status_code=status.HTTP_200_OK,
    tags=["Persons"],
    )
async def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person Id",
        description="This is the Person id field. It's required.",
        example=25,
        )
    ):    # Path(..., gt=0) : int > 0
    persons = [1, 2, 3, 4, 5]
    if person_id not in persons:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    return {"person_id": "Existing person with id: " + str(person_id)}

# Validations: Request body
@app.put(
    "/person/{person_id}",
    status_code = status.HTTP_200_OK,
    tags=["Persons"],
    )
async def update_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person Id",
        description="This is the Person id field. It's required.",
        example=25,
        ),
    person: PersonRequestModel = Body(..., title="Person"),
    # location: Location = Body(..., title="Location")
    ):
    results = person.dict()
    # results.update(location.dict())
    return results

@app.post(
    path="/login",
    response_model=LoginResponseModel,
    status_code = status.HTTP_200_OK,
    tags=["Forms"],
)

# Forms

async def login(
    username: str = Form(..., title="Username"),
    password: str = Form(..., title="Password"),
    ):
    return LoginResponseModel(username=username)

# Cookies and Headers parameters
@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK,
    tags=["Forms"],
    summary="Contact form",
    )
async def contact(
    name: str = Form(..., title="Name"),
    email: str = Form(..., title="Email"),
    message: str = Form(..., title="Message"),
    user_agent: str = Header(default="none"),
    ads_consent: str = Cookie(default="none")
    ):
    """
    # Using Forms, headers and cookies

    ## This path operation is using the Form, Header and Cookie parameters for the contact form.

    ### Parameters:

    - **name: str** -> Name of the person
    - **email: str** -> Email of the person
    :param message: message of the person\n
    :param user_agent: user agent of the system\n
    :param ads_consent: ads consent of the system\n

    ### Returns:
    The user_agent from the web brwser
    """
    return { "user_agent": user_agent }

# Files

@app.post(
    path="/upload",
    status_code=status.HTTP_200_OK,
    tags=["Files"],
    deprecated=True,
    )
async def upload(
    file: UploadFile = File(..., title="File")
    ):
    if not file:
        return {"message": "No file sent"}

    return { "file": file.filename, "format": file.content_type, "size": round(len(file.file.read())/1024,2) }

@app.post(
    path="/uploadfile/",
    status_code=status.HTTP_200_OK,
    tags=["Files"],
    )
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()

    return {"contents": contents}
