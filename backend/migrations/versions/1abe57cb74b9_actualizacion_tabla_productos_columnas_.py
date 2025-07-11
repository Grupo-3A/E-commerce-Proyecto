"""Actualizacion tabla productos columnas no unicas

Revision ID: 1abe57cb74b9
Revises: ee2217677b7e
Create Date: 2025-06-04 13:40:38.706366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1abe57cb74b9'
down_revision = 'ee2217677b7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('productos', schema=None) as batch_op:
        batch_op.drop_constraint('productos_idCategoria_key', type_='unique')
        batch_op.drop_constraint('productos_idMarca_key', type_='unique')
        batch_op.drop_constraint('productos_idTalla_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('productos', schema=None) as batch_op:
        batch_op.create_unique_constraint('productos_idTalla_key', ['idTalla'])
        batch_op.create_unique_constraint('productos_idMarca_key', ['idMarca'])
        batch_op.create_unique_constraint('productos_idCategoria_key', ['idCategoria'])

    # ### end Alembic commands ###
