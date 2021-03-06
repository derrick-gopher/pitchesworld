"""added timestamp field and relationship of comments to user and pitch models

Revision ID: efbc28e229cc
Revises: 933b07b38a47
Create Date: 2018-05-18 23:04:31.580416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efbc28e229cc'
down_revision = '933b07b38a47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('body', sa.Text(), nullable=True))
    op.add_column('comments', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_comments_timestamp'), 'comments', ['timestamp'], unique=False)
    op.drop_index('ix_comments_comment', table_name='comments')
    op.drop_column('comments', 'comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.create_index('ix_comments_comment', 'comments', ['comment'], unique=False)
    op.drop_index(op.f('ix_comments_timestamp'), table_name='comments')
    op.drop_column('comments', 'timestamp')
    op.drop_column('comments', 'body')
    # ### end Alembic commands ###
