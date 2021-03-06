"""empty message

Revision ID: 4368481af247
Revises: 36caacdb6a33
Create Date: 2021-07-30 22:20:12.234403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4368481af247'
down_revision = '36caacdb6a33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test__board', sa.Column('color_option', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test__board', 'color_option')
    # ### end Alembic commands ###
