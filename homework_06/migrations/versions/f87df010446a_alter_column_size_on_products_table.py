"""alter column size on products table

Revision ID: f87df010446a
Revises: 76f6d570eff1
Create Date: 2022-09-12 21:22:47.904733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f87df010446a"
down_revision = "76f6d570eff1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "product",
        "name",
        existing_type=sa.VARCHAR(length=80),
        type_=sa.String(length=100),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "product",
        "name",
        existing_type=sa.String(length=100),
        type_=sa.VARCHAR(length=80),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
