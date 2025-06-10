from typing import Annotated
from src.app.db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

DbDep = Annotated[Session, Depends(get_db)]
