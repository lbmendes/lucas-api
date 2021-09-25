"""
lucas_api base module.
"""
from fastapi import FastAPI, Depends
from .db import init_db, engine, Session, get_session
from .models.user import User, UserList, UserIn, UserOut

app = FastAPI(
    title="Api de Usuários do Lucas",
    version="0.1.0",
    on_startup=[init_db]
)

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/user", response_model=UserList)
def list_users():
    with Session(engine) as session:
        return session.query(User).all()


@app.post("/user", response_model=UserOut)
def create_user(user: UserIn, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.delete("/user")
def delete_user(userid: int, session: Session = Depends(get_session)):
    user = session.get(User, userid)
    session.delete(user)
    session.commit()
    return {"ok": "user deleted"}