from .user import User
from .datetime_utils import now
from .base_model import BaseModel
from playhouse.postgres_ext import (
    ForeignKeyField, CharField, BooleanField, DateTimeTZField
)

class Appeal(BaseModel):
    patient = ForeignKeyField(
        backref="appeals", column_name="user_id",
        field="id", model=User, null=False
    )
    therapist = ForeignKeyField(
        backref="appeals", column_name="user_id",
        field="id", model=User, null=True
    )
    created_at = DateTimeTZField(index=True, default=now)
    connection_type = CharField(null=False, max_length=100)
    is_taken = BooleanField(default=False)

    class Meta:
        table_name = "appeal"
