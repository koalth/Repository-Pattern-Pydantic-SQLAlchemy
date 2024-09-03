from pydantic import BaseModel, Field
from datetime import datetime
import uuid
from typing import Optional, List, Generic, TypeVar, Type
from sqlalchemy import select, delete
from .model import Base
from .session import sessionmanager

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
EntityType = TypeVar("EntityType", bound=BaseModel)

class GenericRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType, EntityType]):
    def __init__(self, model: Type[ModelType], entity: Type[EntityType]):
        self.model = model
        self.entity = entity
        
    async def create(self, obj_in: CreateSchemaType) -> EntityType:
        db_obj = self.model(**obj_in.model_dump())
        async with sessionmanager.session() as session:
            session.add(db_obj)
            await session.commit()
            await session.refresh(db_obj)
            return self.entity.model_validate(db_obj)
        
    async def get(self, id: uuid.UUID) -> EntityType:
        stmt = select(self.model).where(self.model.id == id)
        async with sessionmanager.session() as session:
            results = await session.execute(stmt)
            obj = results.scalar_one()
            return self.entity.model_validate(obj)
        
    async def get_all(self, *filter_conditions) -> List[EntityType]:
        stmt = select(self.model)
        if filter_conditions:
            stmt = stmt.where(*filter_conditions)
        async with sessionmanager.session() as session:
            results = await session.execute(stmt)
            return [self.entity.model_validate(obj) for obj in results.scalars().all()]
        
    async def update(self, id: uuid.UUID, obj_in: UpdateSchemaType) -> EntityType:
        stmt = select(self.model).where(self.model.id == id)
        async with sessionmanager.session() as session:
            results = await session.execute(stmt)
            db_obj = results.scalar_one()
            update_data = obj_in.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_obj, key, value)
            await session.commit()
            await session.refresh(db_obj)
            return self.entity.model_validate(db_obj)
        
    async def delete(self, id: uuid.UUID) -> bool:
        stmt = delete(self.model).where(self.model.id == id)
        async with sessionmanager.session() as session:
            results = await session.execute(stmt)
            await session.commit()
            return results.rowcount > 0
        
        
        