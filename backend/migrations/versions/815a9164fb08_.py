"""Initial doctors and patients tables migration

Revision ID: 815a9164fb08
Revises: 
Create Date: 2020-07-13 09:25:18.589795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '815a9164fb08'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctors',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('age', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('patients',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('age', sa.Integer(), nullable=False),
                    sa.Column('gender', sa.String(), nullable=False),
                    sa.Column('medication', sa.String(), nullable=True),
                    sa.Column('doctor_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patients')
    op.drop_table('doctors')
    # ### end Alembic commands ###
