"""Delete on cascade migration

Revision ID: bfd5763550ae
Revises: da10b68aac58
Create Date: 2025-09-06 23:32:08.618814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bfd5763550ae'
down_revision: Union[str, Sequence[str], None] = 'da10b68aac58'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint(op.f('answers_question_id_fkey'), 'answers', type_='foreignkey')
    op.create_foreign_key(None, 'answers', 'questions', ['question_id'], ['id'], ondelete='CASCADE')


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(None, 'answers', type_='foreignkey')
    op.create_foreign_key(op.f('answers_question_id_fkey'), 'answers', 'questions', ['question_id'], ['id'])
