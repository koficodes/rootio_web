"""change_program

Revision ID: 54176dfaa1f4
Revises: 14665e1003a2
Create Date: 2016-09-16 11:42:06.099741

"""

# revision identifiers, used by Alembic.
revision = '54176dfaa1f4'
down_revision = '14665e1003a2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('radio_program', sa.Column('content_type_id', sa.Integer(), nullable=True))
    op.drop_column('radio_program', u'program_type_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('radio_program', sa.Column(u'program_type_id', sa.INTEGER(), nullable=True))
    op.drop_column('radio_program', 'content_type_id')
    ### end Alembic commands ###