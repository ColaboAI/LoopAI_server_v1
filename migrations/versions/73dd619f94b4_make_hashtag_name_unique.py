"""Make hashtag name unique

Revision ID: 73dd619f94b4
Revises: ef9ec3e8bd60
Create Date: 2022-09-06 15:51:11.096754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73dd619f94b4'
down_revision = 'ef9ec3e8bd60'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'hashtag', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'hashtag', type_='unique')
    # ### end Alembic commands ###