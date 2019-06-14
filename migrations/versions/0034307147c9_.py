"""empty message

Revision ID: 0034307147c9
Revises: fd713f6e45cb
Create Date: 2019-06-14 09:08:33.984011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0034307147c9'
down_revision = 'fd713f6e45cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercisetype', schema=None) as batch_op:
        batch_op.add_column(sa.Column('etuid', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['etuid'], ['uid'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercisetype', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('etuid')

    # ### end Alembic commands ###
