"""empty message

Revision ID: 51fd5c8b1ee7
Revises: f596648fb4b2
Create Date: 2020-04-14 03:34:28.714194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51fd5c8b1ee7'
down_revision = 'f596648fb4b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('government',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('point_of_contact', sa.String(length=128), nullable=True),
    sa.Column('sub_category', sa.String(length=64), nullable=True),
    sa.Column('email_id_1', sa.String(length=128), nullable=True),
    sa.Column('email_id_2', sa.String(length=128), nullable=True),
    sa.Column('phone_1', sa.String(length=128), nullable=True),
    sa.Column('phone_2', sa.String(length=128), nullable=True),
    sa.Column('source_url', sa.String(length=512), nullable=True),
    sa.Column('source', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.ForeignKeyConstraint(['state_id'], ['state.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('government')
    # ### end Alembic commands ###
