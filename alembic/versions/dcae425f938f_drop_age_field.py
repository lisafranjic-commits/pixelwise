"""Drop age field

Revision ID: dcae425f938f
Revises: d025edc9bbea
Create Date: 2026-06-16 17:02:39.859111

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dcae425f938f'
down_revision: Union[str, Sequence[str], None] = 'd025edc9bbea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_column('person', 'age')


def downgrade():
    op.add_column('person', sa.Column('age', sa.Integer(), primary_key=False))
