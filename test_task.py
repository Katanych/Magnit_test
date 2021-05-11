'''Программа, тестирующая функцию подсчета отпускной цены'''
from selling_price import calculate_selling_price

def main():
    '''Тестирование программы'''
    while True:
        try:
            num_prod = int(input("Введите кол-во продуктов: "))
            products = dict()
            for _ in range(num_prod):
                name_prod = input("\nНазвание продкута: ")
                products[name_prod] = float(input("Цена продукта: "))
            break
        except ValueError:
            print("Хей! Тебе вроде необходимо ввести число. Повтори попытку.\n")
        except Exception:
            print("Это еще что такое?\n")
    print("\nОтпускная цена:", calculate_selling_price(products))


if __name__ == "__main__":
    main()
    