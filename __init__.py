from trytond.pool import Pool

__all__ = ['register']


def register():
    Pool.register(
        module='product_cost_bom', type_='model')
    Pool.register(
        module='product_cost_bom', type_='wizard')
    Pool.register(
        module='product_cost_bom', type_='report')
