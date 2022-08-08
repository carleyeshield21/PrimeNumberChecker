def prime_checker(number = int(input('Type any number: '))):
    # print(number, type(number))
    counter = 0
    for i in range(1, number + 1):
        # print(i)
        remainder = number % i
        # print(remainder, i)
        if remainder == 0:
            counter += 1
    # print(counter)
    if counter <= 2:
        print(f'{number} is a Prime Number')
    else:
        print(f'{number} is a Composite Number')
prime_checker()