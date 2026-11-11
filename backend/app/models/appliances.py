
from datetime import datetime, timezone

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class ApplianceCategory(Base):
    __tablename__ = "appliance_categories"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )

    name: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False
    )

    appliances: Mapped[list["Appliance"]] = relationship(
        back_populates="category"
    )


class Appliance(Base):
    __tablename__ = "appliances"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )

    home_id: Mapped[int] = mapped_column(
        ForeignKey("homes.id"), nullable=False
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("appliance_categories.id"), nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(150), nullable=False
    )

    brand: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    model_number: Mapped[str | None] = mapped_column(
    String(100), nullable=True
    )
    
    purchase_date: Mapped[datetime | None] = mapped_column(
    DateTime, nullable=True
    )
    
    warranty_expiry: Mapped[datetime | None] = mapped_column(
    DateTime, nullable=True
    )
    
    notes: Mapped[str | None] = mapped_column(
    Text, nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    category: Mapped["ApplianceCategory"] = relationship(
        back_populates="appliances"
    )

    documents: Mapped[list["ApplianceDocument"]] = relationship(
        back_populates="appliance",
        cascade="all, delete-orphan"
    )


class ApplianceDocument(Base):
    __tablename__ = "appliance_documents"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )

    appliance_id: Mapped[int] = mapped_column(
        ForeignKey("appliances.id"), nullable=False
    )

    document_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )

    file_name: Mapped[str] = mapped_column(
        String(255), nullable=False
    )

    file_path: Mapped[str] = mapped_column(
        String(500), nullable=False
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    appliance: Mapped["Appliance"] = relationship(
        back_populates="documents"
    )
