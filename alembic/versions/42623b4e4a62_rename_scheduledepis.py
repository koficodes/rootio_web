"""rename ScheduledEpisode to ScheduledProgram

Revision ID: 42623b4e4a62
Revises: 57cff29eadbf
Create Date: 2013-10-26 21:53:48.514719

"""

# revision identifiers, used by Alembic.
revision = '42623b4e4a62'
down_revision = '57cff29eadbf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    #rename instead of add/drop, because of existing fk constraints
    op.rename_table('radio_scheduledprogram','radio_scheduledepisode')
    op.rename_table('onair_program','onair_episode')

    op.alter_column(u'telephony_call', 'onairepisode_id', new_column_name='onairprogram_id')
    op.alter_column(u'telephony_message', 'onairepisode_id', new_column_name='onairprogram_id')

    op.drop_table(u'radio_blockedprogram')

def downgrade():
    #rename instead of add/drop, because of existing fk constraints
    op.rename_table('radio_scheduledepisode','radio_scheduledprogram')
    op.rename_table('onair_episode','onair_program')

    op.alter_column(u'telephony_call', 'onairprogram_id', new_column_name='onairepisode_id')
    op.alter_column(u'telephony_message', 'onairprogram_id', new_column_name='onairepisode_id')

    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(u'radio_blockedprogram',
    sa.Column(u'id', sa.INTEGER(), nullable=False),
    sa.Column(u'station_id', sa.INTEGER(), nullable=True),
    sa.Column(u'program_id', sa.INTEGER(), nullable=True),
    sa.Column(u'block_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['block_id'], [u'radio_scheduledblock.id'], ),
    sa.ForeignKeyConstraint(['program_id'], [u'radio_program.id'], ),
    sa.ForeignKeyConstraint(['station_id'], [u'radio_station.id'], ),
    sa.PrimaryKeyConstraint(u'id')
    )
    ### end Alembic commands ###