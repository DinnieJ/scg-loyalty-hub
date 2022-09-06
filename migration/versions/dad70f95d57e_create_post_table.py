"""create post table

Revision ID: dad70f95d57e
Revises: 25e9c84b4258
Create Date: 2022-09-06 10:27:40.402041

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import TIMESTAMP, TEXT


# revision identifiers, used by Alembic.
revision = 'dad70f95d57e'
down_revision = '25e9c84b4258'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'scg_posts',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement='ignore_fk'),
        sa.Column('title', sa.String(255), nullable=True),
        sa.Column('user_id', sa.BigInteger, nullable=False),
        sa.Column('content', sa.Text, nullable=True),
        sa.Column('created_at', TIMESTAMP(), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        )
    )

    op.create_index(index_name="idx_user_id", table_name="scg_posts", columns=["user_id"])
    op.create_foreign_key(
        "fk_user_id",
        source_table="scg_posts",
        referent_table="scg_users",
        local_cols=["user_id"],
        remote_cols=["id"]
    )


def downgrade() -> None:
    op.drop_table("scg_posts")
