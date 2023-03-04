"""create_customers_table

Revision ID: 68acf1742ddb
Revises: cf14ec9ea601
Create Date: 2023-03-01 22:50:53.909968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68acf1742ddb'
down_revision = 'cf14ec9ea601'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "customers",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    )


def downgrade():
    op.drop_table('customers')