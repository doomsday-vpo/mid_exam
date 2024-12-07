def get_initial_products():
    return input().split("|")


def handle_important(products, product):
    if product in products:
        products.remove(product)
    products.insert(0, product)
    return products


def handle_add(products, product):
    if product not in products:
        products.append(product)
    else:
        print("The product is already in the list.")
    return products


def handle_swap(products, product1, product2):
    if product1 not in products:
        print(f"Product {product1} missing!")
    elif product2 not in products:
        print(f"Product {product2} missing!")
    else:
        index1 = products.index(product1)
        index2 = products.index(product2)
        products[index1], products[index2] = products[index2], products[index1]
    return products


def handle_remove(products, product):
    if product in products:
        products.remove(product)
    else:
        print(f"Product {product} isn't in the list.")
    return products


def process_command(products, command):
    tokens = command.split("%")
    action = tokens[0]

    if action == "Important":
        products = handle_important(products, tokens[1])
    elif action == "Add":
        products = handle_add(products, tokens[1])
    elif action == "Swap":
        products = handle_swap(products, tokens[1], tokens[2])
    elif action == "Remove":
        products = handle_remove(products, tokens[1])
    elif action == "Reversed":
        products.reverse()

    return products


def print_final_list(products):
    for i in range(len(products)):
        print(f"{i + 1}. {products[i]}")


def main():
    products = get_initial_products()
    command = input()

    while command != "Shop!":
        products = process_command(products, command)
        command = input()

    print_final_list(products)


if __name__ == "__main__":
    main()
