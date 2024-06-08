"""adding one column

Revision ID: ad386c6fb161
Revises: 
Create Date: 2024-06-06 21:21:25.334639

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad386c6fb161'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('liked', sa.Boolean(), nullable=False, server_default='TRUE'))
    pass

    
def downgrade():
    op.drop_column('posts', 'liked')
    pass
