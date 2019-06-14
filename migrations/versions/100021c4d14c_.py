"""empty message

Revision ID: 100021c4d14c
Revises: a4a9fa4fe35d
Create Date: 2019-06-14 09:17:25.218136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '100021c4d14c'
down_revision = 'a4a9fa4fe35d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercisetype', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uid', sa.Integer(), nullable=True))
        batch_op.drop_constraint('exercisetype_id', type_='foreignkey')
        batch_op.create_foreign_key("exercisetype_uid", 'user', ['uid'], ['uid'])
        batch_op.drop_column('etid')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercisetype', schema=None) as batch_op:
        batch_op.add_column(sa.Column('etid', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('exercisetype_id', 'user', ['etid'], ['uid'])
        batch_op.drop_column('uid')

    # ### end Alembic commands ###
