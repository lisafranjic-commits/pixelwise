"""Seed person table

Revision ID: d025edc9bbea
Revises: 9ecf51739d94
Create Date: 2026-06-16 16:44:47.839217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd025edc9bbea'
down_revision: Union[str, Sequence[str], None] = '9ecf51739d94'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.bulk_insert(
        sa.table(
            'person',
            sa.column('id', sa.Integer),
            sa.column('forename', sa.String),
            sa.column('surname', sa.String),
            sa.column('age', sa.Integer),
        ),
        [
            {'id': 1, 'forename': 'Max', 'surname': 'Mustermann', 'age': 30},
            {'id': 2, 'forename': 'Anna', 'surname': 'Schmidt', 'age': 23},
            {'id': 3, 'forename': 'Thomas', 'surname': 'Müller', 'age': 47},
        ]
    )


def downgrade():
    op.execute("DELETE FROM person WHERE id IN (1,2,3)")

