"""xui znaet

Revision ID: 2998bba34c69
Revises: 52f9b01ada86
Create Date: 2021-08-05 13:42:13.806995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2998bba34c69'
down_revision = '52f9b01ada86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id_messaage', sa.Integer(), nullable=False),
    sa.Column('user_nick', sa.String(length=100), nullable=True),
    sa.Column('send_to', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_nick'], ['users.nick'], ),
    sa.PrimaryKeyConstraint('id_messaage')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
