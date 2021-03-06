"""followers

Revision ID: 276e18ffb0c9
Revises: 1532aab9d300
Create Date: 2021-02-18 14:46:25.170659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '276e18ffb0c9'
down_revision = '1532aab9d300'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
