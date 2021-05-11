'''Подсчет отпускной цены'''


def calculate_selling_price(products: dict):
    '''Функция подсчета цены для продажи
    Сперва цена товара округлена до целого числа,
    затем скорректирована так, чтобы последняя цифра
    была 5 или 0.

    '''
    for key in products.keys():
        products[key] *= 1.15
        round(products[key], 0)
        products[key] = 5 * round(products[key]/5)
    return products
