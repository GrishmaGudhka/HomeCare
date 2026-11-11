
from datetime import datetime, timezone

from sqlalchemy import (
    String,
    Integer,
    Boolean,
    DateTime,
    ForeignKey,
    UniqueConstraint
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


# -------------------------
# USER MODEL
# -------------------------

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )

    full_name: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(
        String(150), unique=True, index=True, nullable=False
    )
    
    phone: Mapped[str | None] = mapped_column(
    String(15), nullable=True
    )
    
    hashed_password: Mapped[str] = mapped_column(
        String(255), nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    home_memberships: Mapped[list["HomeMember"]] = relationship(
        back_populates="user"
    )


# -------------------------
# HOME MODEL
# -------------------------

class Home(Base):
    __tablename__ = "homes"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    address: Mapped[str] = mapped_column(String(255), nullable=False)

    city: Mapped[str] = mapped_column(String(100), nullable=False)

    state: Mapped[str] = mapped_column(String(100), nullable=False)

    pincode: Mapped[str] = mapped_column(String(10), nullable=False)

    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    members: Mapped[list["HomeMember"]] = relationship(
        back_populates="home"
    )


# -------------------------
# HOME MEMBER MODEL
# -------------------------

class HomeMember(Base):
    __tablename__ = "home_members"

    __table_args__ = (
        UniqueConstraint(
            "user_id", "home_id",
            name="unique_user_home"
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False
    )

    home_id: Mapped[int] = mapped_column(
        ForeignKey("homes.id"), nullable=False
    )

    role: Mapped[str] = mapped_column(
        String(30), default="MEMBER"
    )

    joined_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True
    )

    user: Mapped["User"] = relationship(
        back_populates="home_memberships"
    )

    home: Mapped["Home"] = relationship(
        back_populates="members"
    )
