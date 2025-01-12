"""create price column

Revision ID: 097ca1459da5
Revises: eb772e742dbd
Create Date: 2023-06-26 12:19:57.244765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '097ca1459da5'
down_revision = 'eb772e742dbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.drop_column('price')

    # ### end Alembic commands ###
