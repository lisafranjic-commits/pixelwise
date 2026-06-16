"""create person table

Revision ID: 9f1f9a907ac9
Revises: 
Create Date: 2026-06-16 16:21:29.363141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f1f9a907ac9'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'person',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('forename', sa.String(50), nullable=False),
        sa.Column('surname', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('person')

