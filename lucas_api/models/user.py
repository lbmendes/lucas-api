from sqlmodel import SQLModel, Field
from typing import Optional, List
from pydantic import validator

# --- model ---

class User(SQLModel, table=True):
    id: Optional[int] = Field(None, primary_key=True)
    username: str
    password: str


# --- serializers ---


class UserOut(SQLModel):
    username: str


class UserIn(SQLModel):
    username: str
    password: str
    confirm_password: str

#    @validator(confirm_password)
#    def validate_password(cls, v, values):
#        if v and v != values['password']:
#            raise ValueError("aaaa")
#        return v


UserList = List[UserOut]