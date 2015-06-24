def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product *= i
    return product

prod = calcProd()

print('The result is {} digits long.'.format(len(str(prod))))