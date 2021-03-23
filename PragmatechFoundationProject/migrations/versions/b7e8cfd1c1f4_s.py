"""S

Revision ID: b7e8cfd1c1f4
Revises: 
Create Date: 2021-03-22 22:08:01.742385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7e8cfd1c1f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Profileinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('infoname', sa.String(length=30), nullable=True),
    sa.Column('info', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Profileinfo')
    # ### end Alembic commands ###
