"""Change to DateTime, and reset all previous migrations

Revision ID: befaf523bebb
Revises: 
Create Date: 2021-10-21 15:14:46.169545

"""
import fastapi_users_db_sqlalchemy
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'befaf523bebb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', fastapi_users_db_sqlalchemy.GUID(), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=72), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('login', sa.String(), nullable=True),
    sa.Column('reg_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('term', sa.String(), nullable=True),
    sa.Column('value', sa.String(), nullable=True),
    sa.Column('repeats', sa.Integer(), nullable=True, default=0),
    sa.Column('active', sa.Boolean(), nullable=True, default=True),
    sa.Column('create_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('user', fastapi_users_db_sqlalchemy.GUID(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cards_id'), 'cards', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cards_id'), table_name='cards')
    op.drop_table('cards')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
