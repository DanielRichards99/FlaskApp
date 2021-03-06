"""new fields in user model

Revision ID: 1532aab9d300
Revises: ce69df1cd3b0
Create Date: 2021-02-18 11:51:22.630950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1532aab9d300'
down_revision = 'ce69df1cd3b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
