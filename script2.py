import random
from pydantic import BaseModel, Field, validator



class User(BaseModel):
    username: str
    password: int = Field(default_factory=lambda: random.randint(1, 10))

    @validator("username")
    def validate_username(cls, v):
        if v == 'bruno':
            raise ValueError("Não pode ter bruno")
        return v
    
user = User(username="admin")

print(user.username)
print(user.password)
