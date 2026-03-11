#Write a program to make use of map(), filter() and reduce() functions with context to lambda functions.


from functools import reduce

def main():
   
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original List: {numbers}")
    print("-" * 30)

   
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    
    print(f"1. Map (Squared): {squared_numbers}")
   
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    print(f"2. Filter (Evens): {even_numbers}")
    
    product_of_all = reduce(lambda x, y: x * y, numbers)
    
    print(f"3. Reduce (Product): {product_of_all}")
   

if __name__ == "__main__":
    main()
