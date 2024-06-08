"""adding the user table

Revision ID: 3f8922a77c06
Revises: daedba1eaa03
Create Date: 2024-06-08 20:25:41.850806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f8922a77c06'
down_revision: Union[str, None] = 'daedba1eaa03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String(), unique=True, index=True),
        sa.Column('hashed_password', sa.String()),
    )


def downgrade() -> None:
    op.drop_table('users')