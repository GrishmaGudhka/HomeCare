from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.core import Home, HomeMember, User
from app.schemas.home import HomeCreate, HomeResponse
from app.services.authentication import get_current_user


router = APIRouter(
    prefix="/homes",
    tags=["Property Management"]
)


# CREATE A NEW PROPERTY
@router.post(
    "/",
    response_model=HomeResponse,
    status_code=status.HTTP_201_CREATED
)
def create_home(
    home_data: HomeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Create the property
    new_home = Home(
        name=home_data.name,
        address=home_data.address,
        city=home_data.city,
        state=home_data.state,
        pincode=home_data.pincode,
        created_by=current_user.id
    )

    db.add(new_home)
    db.flush()

    # Add the creator as the property's owner
    membership = HomeMember(
        user_id=current_user.id,
        home_id=new_home.id,
        role="OWNER"
    )

    db.add(membership)
    db.commit()
    db.refresh(new_home)

    return new_home


# VIEW ALL PROPERTIES OF THE LOGGED-IN USER
@router.get(
    "/",
    response_model=list[HomeResponse]
)
def get_my_homes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    homes = db.scalars(
        select(Home)
        .join(HomeMember, Home.id == HomeMember.home_id)
        .where(
            HomeMember.user_id == current_user.id,
            HomeMember.is_active.is_(True)
        )
    ).all()

    return homes