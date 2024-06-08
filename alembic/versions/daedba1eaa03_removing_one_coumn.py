"""Removing one coumn

Revision ID: daedba1eaa03
Revises: ad386c6fb161
Create Date: 2024-06-08 19:46:22.667874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'daedba1eaa03'
down_revision: Union[str, None] = 'ad386c6fb161'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_column('posts', 'liked')
    pass


def downgrade():
    op.add_column('posts', sa.Column('liked', sa.Boolean(), nullable=False, server_default='TRUE'))
    pass
