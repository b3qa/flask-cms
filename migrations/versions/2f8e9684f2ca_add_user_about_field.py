"""add user about field

Revision ID: 2f8e9684f2ca
Revises: 142b6f7bfc93
Create Date: 2025-02-07 13:56:33.838460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f8e9684f2ca'
down_revision = '142b6f7bfc93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
