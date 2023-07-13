"""empty message

Revision ID: 9e4ef4e5d15a
Revises: fe09730c4d8d
Create Date: 2023-07-13 20:40:48.392814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e4ef4e5d15a'
down_revision = 'fe09730c4d8d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ds', sa.Column('data', sa.String(length=256), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ds', 'data')
    # ### end Alembic commands ###
