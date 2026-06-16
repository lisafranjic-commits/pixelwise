"""Add a column

Revision ID: 9ecf51739d94
Revises: 9f1f9a907ac9
Create Date: 2026-06-16 16:38:13.831111

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ecf51739d94'
down_revision: Union[str, Sequence[str], None] = '9f1f9a907ac9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        'person',
        sa.Column('age', sa.Integer, primary_key=False),
    )


def downgrade():
    op.drop_column('person', 'age')

