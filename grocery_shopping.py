# On the first line, you will receive a sequence with products, split by "|". On the following lines, until command "Shop!",
# you will be receiving commands. The possible commands are:
# •	"Important%{product}":
# o	If the product exists, move it to the beginning of the list (index 0).
# o	Otherwise, add it to the list at the 0 index.
# •	"Add%{product}":
# o	If the product did not exist – add it at the end of the list.
# o	Otherwise, print: "The product is already in the list."
# •	"Swap%{product}%{product}":
# o	If both products exist – swap their places.
# o	If one of the two products is missing, print: "Product {product} missing!"
# o	There is no case in which both products are missing at the same time.
# •	"Remove%{product}":
# o	If the product is in the list, remove it.
# o	Otherwise, print: "Product {product} isn't in the list."
# •	"Reversed":
# o	Reverse the list of products.
# When you receive the command "Shop!" you should print each product from the list on a new line with its number in the list (starting from 1) and end the program:
# "1. {product1}
# 2. {product2}
# …
# N. {productN}"
# Input
# •	On the first line, you will receive a sequence with products, split by "|".
# •	On the following lines, until the command "Shop!", you will be receiving commands.
# Output
# •	Print the output needed as described above.


products = input().split("|")
command = input()

while command != "Shop!":
    tokens = command.split("%")
    action = tokens[0]

    if action == "Important":
        product = tokens[1]
        if product in products:
            products.remove(product)
            products.insert(0, product)
        else:
            products.insert(0, product)

    elif action == "Add":
        product = tokens[1]
        if product not in products:
            products.append(product)
        else:
            print("The product is already in the list.")

    elif action == "Swap":
        product1 = tokens[1]
        product2 = tokens[2]
        if product1 not in products:
            print(f"Product {product1} missing!")
        elif product2 not in products:
            print(f"Product {product2} missing!")
        else:
            index1 = products.index(product1)
            index2 = products.index(product2)
            products[index1], products[index2] = products[index2], products[index1]

    elif action == "Remove":
        product = tokens[1]
        if product in products:
            products.remove(product)
        else:
            print(f"Product {product} isn't in the list.")

    elif action == "Reversed":
        products.reverse()

    command = input()

for i in range(len(products)):
    print(f"{i + 1}. {products[i]}")
