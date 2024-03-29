"""empty message

Revision ID: f21eda6fd939
Revises: 14f93867441d
Create Date: 2024-02-05 16:04:52.816305

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f21eda6fd939'
down_revision = '14f93867441d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data', schema=None) as batch_op:
        batch_op.alter_column('duedate',
               existing_type=mysql.DATETIME(),
               type_=sa.String(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data', schema=None) as batch_op:
        batch_op.alter_column('duedate',
               existing_type=sa.String(length=100),
               type_=mysql.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
