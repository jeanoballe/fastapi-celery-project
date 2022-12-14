"""empty message

Revision ID: 45c618a18f1e
Revises: b00f8d66166f
Create Date: 2022-12-01 17:14:51.764436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45c618a18f1e'
down_revision = 'b00f8d66166f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
