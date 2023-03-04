"""create_customers_cars_table

Revision ID: 78b38fc02927
Revises: 68acf1742ddb
Create Date: 2023-03-01 22:51:40.797228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78b38fc02927'
down_revision = '68acf1742ddb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "customers_cars",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column('color', sa.String(255), nullable=False),
        sa.Column('type', sa.String(255), nullable=False),
        sa.Column('customer_id', sa.BigInteger, sa.ForeignKey('customers.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    )


def downgrade():
    op.drop_table('customers_cars')