"""empty message

Revision ID: 6349e7255203
Revises: 
Create Date: 2023-05-26 16:10:00.928378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6349e7255203'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('persona',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido', sa.String(length=250), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=True),
    sa.Column('telefono', sa.String(length=250), nullable=True),
    sa.Column('sintomas', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('persona')
    # ### end Alembic commands ###
