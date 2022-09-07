"""Add music table

Revision ID: 2cae7a638ed6
Revises: bbe7f24d59f0
Create Date: 2022-09-03 15:14:38.729704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cae7a638ed6'
down_revision = 'bbe7f24d59f0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('artist_name', sa.String(length=100), nullable=False),
    sa.Column('audio_url', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_audio_id'), 'audio', ['id'], unique=False)
    op.create_table('hashtag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hashtag_id'), 'hashtag', ['id'], unique=False)
    op.create_table('association',
    sa.Column('audio_id', sa.Integer(), nullable=False),
    sa.Column('hashtag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['audio_id'], ['audio.id'], ),
    sa.ForeignKeyConstraint(['hashtag_id'], ['hashtag.id'], ),
    sa.PrimaryKeyConstraint('audio_id', 'hashtag_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_index(op.f('ix_hashtag_id'), table_name='hashtag')
    op.drop_table('hashtag')
    op.drop_index(op.f('ix_audio_id'), table_name='audio')
    op.drop_table('audio')
    # ### end Alembic commands ###