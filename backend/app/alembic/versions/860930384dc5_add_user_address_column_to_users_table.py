"""Add user_address column to users table

Revision ID: 860930384dc5
Revises: 3dd78c16aa76
Create Date: 2025-01-08 16:21:27.336720

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '860930384dc5'
down_revision: Union[str, None] = '3dd78c16aa76'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add user_address column to users table
    op.add_column('users', sa.Column('user_address', sa.String(length=255), nullable=True))
    
    


def downgrade() -> None:
    # Drop user_address column from users table
    op.drop_column('users', 'user_address')