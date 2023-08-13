"""add_good

Revision ID: d7d5d27f6c9f
Revises:
Create Date: 2023-08-13 15:22:32.881134

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'd7d5d27f6c9f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('create schema stone')
    op.create_table(
        't_good',
        sa.Column('id_good', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=250), nullable=False),
        sa.PrimaryKeyConstraint('id_good'),
        schema='stone',
        comment='Goods'
    )
    op.create_index(op.f('ix_stone_t_good_id_good'), 't_good', ['id_good'], unique=False, schema='stone')


def downgrade() -> None:
    op.drop_index(op.f('ix_stone_t_good_id_good'), table_name='t_good', schema='stone')
    op.drop_table('t_good', schema='stone')
    op.execute('drop schema stone')
