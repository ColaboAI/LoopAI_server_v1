"""Change association table name

Revision ID: ef9ec3e8bd60
Revises: 2cae7a638ed6
Create Date: 2022-09-03 15:28:29.357168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef9ec3e8bd60'
down_revision = '2cae7a638ed6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audio_hashtag_association',
    sa.Column('audio_id', sa.Integer(), nullable=False),
    sa.Column('hashtag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['audio_id'], ['audio.id'], ),
    sa.ForeignKeyConstraint(['hashtag_id'], ['hashtag.id'], ),
    sa.PrimaryKeyConstraint('audio_id', 'hashtag_id')
    )
    op.drop_table('association')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('association',
    sa.Column('audio_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('hashtag_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['audio_id'], ['audio.id'], name='association_audio_id_fkey'),
    sa.ForeignKeyConstraint(['hashtag_id'], ['hashtag.id'], name='association_hashtag_id_fkey'),
    sa.PrimaryKeyConstraint('audio_id', 'hashtag_id', name='association_pkey')
    )
    op.drop_table('audio_hashtag_association')
    # ### end Alembic commands ###
