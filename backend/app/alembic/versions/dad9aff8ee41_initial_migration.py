"""Initial migration

Revision ID: dad9aff8ee41
Revises: 
Create Date: 2025-01-08 16:13:21.552838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'dad9aff8ee41'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add user_address column to users table
    op.add_column('users', sa.Column('user_address', sa.String(length=255), nullable=True))
    
    


def downgrade() -> None:
    # Drop user_address column from users table
    op.drop_column('users', 'user_address')
