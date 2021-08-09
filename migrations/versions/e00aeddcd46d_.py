"""empty message

Revision ID: e00aeddcd46d
Revises: a3c04b7a0053
Create Date: 2021-08-09 20:42:33.832013

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e00aeddcd46d'
down_revision = 'a3c04b7a0053'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False,
               autoincrement=True)
    op.alter_column('s18_1', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False,
               autoincrement=True)
    op.alter_column('s18_2', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False,
               autoincrement=True)
    op.alter_column('s18_s', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False,
               autoincrement=True)
    op.alter_column('s18_w', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False,
               autoincrement=True)
    op.alter_column('s19_1', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False,
               autoincrement=True)
    op.alter_column('s19_2', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False,
               autoincrement=True)
    op.alter_column('s19_s', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False,
               autoincrement=True)
    op.alter_column('s19_w', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('s19_w', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True,
               autoincrement=True)
    op.alter_column('s19_s', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True,
               autoincrement=True)
    op.alter_column('s19_2', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True,
               autoincrement=True)
    op.alter_column('s19_1', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True,
               autoincrement=True)
    op.alter_column('s18_w', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True,
               autoincrement=True)
    op.alter_column('s18_s', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True,
               autoincrement=True)
    op.alter_column('s18_2', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True,
               autoincrement=True)
    op.alter_column('s18_1', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True,
               autoincrement=True)
    op.alter_column('departments', 'id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True,
               autoincrement=True)
    # ### end Alembic commands ###
