"""adding users table

Revision ID: 76cf64c8dd3e
Revises: 6d5c13f46eab
Create Date: 2024-06-15 13:41:38.952273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76cf64c8dd3e'
down_revision: Union[str, None] = '6d5c13f46eab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String, nullable=False),
        sa.Column('hashed_password', sa.String, nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
