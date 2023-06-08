"""password lenght

Revision ID: 446c646434d0
Revises: fd4bc0ddcfb4
Create Date: 2023-06-05 15:54:54.813732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '446c646434d0'
down_revision = 'fd4bc0ddcfb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)

    # ### end Alembic commands ###
