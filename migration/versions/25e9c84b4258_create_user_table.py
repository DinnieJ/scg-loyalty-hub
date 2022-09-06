"""create user table

Revision ID: 25e9c84b4258
Revises: 
Create Date: 2022-09-06 10:26:09.956846

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import TIMESTAMP

# revision identifiers, used by Alembic.
revision = '25e9c84b4258'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("scg_users",
                    sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
                    sa.Column('email', sa.String(100), nullable=False, unique=True),
                    sa.Column('name', sa.String(255), nullable=False),
                    sa.Column('password', sa.String(64), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP, server_default=sa.text("CURRENT_TIMESTAMP")),
                    sa.Column('updated_at', sa.TIMESTAMP,
                              server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                              )
                    )
    pass


def downgrade() -> None:
    op.drop_table("scg_users")
