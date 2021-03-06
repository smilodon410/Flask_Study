"""empty message

Revision ID: 16cb645e196a
Revises: 2fb6a8f6b295
Create Date: 2021-02-16 16:13:01.261980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16cb645e196a'
down_revision = '2fb6a8f6b295'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
