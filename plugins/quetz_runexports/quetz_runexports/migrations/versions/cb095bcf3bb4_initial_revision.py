"""initial revision

Revision ID: cb095bcf3bb4
Revises: a80fb051a659
Create Date: 2020-11-25 00:14:48.269216

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "cb095bcf3bb4"
down_revision = None
branch_labels = ("quetz-runexports",)
depends_on = "a80fb051a659"


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "quetz_runexports_package_version_metadata",
        sa.Column("version_id", sa.LargeBinary(length=16), nullable=False),
        sa.Column("data", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["version_id"],
            ["package_versions.id"],
        ),
        sa.PrimaryKeyConstraint("version_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("quetz_runexports_package_version_metadata")
    # ### end Alembic commands ###
