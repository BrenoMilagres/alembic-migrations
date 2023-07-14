"""add_columns

Revision ID: 70a5d8afb0cf
Revises: 1d97a16bb830
Create Date: 2023-07-14 14:50:15.208896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70a5d8afb0cf'
down_revision = '1d97a16bb830'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ae', sa.Column('bi', sa.String(length=256), nullable=False))
    op.add_column('de', sa.Column('code', sa.String(length=256), nullable=False))
    op.add_column('ds', sa.Column('ml', sa.String(length=256), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ds', 'ml')
    op.drop_column('de', 'code')
    op.drop_column('ae', 'bi')
    # ### end Alembic commands ###
