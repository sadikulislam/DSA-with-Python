   # Drop constant  time complexity: O(2n) => O(n)

def print_items(n):
    for i in range (n):
        print(i)

    for j in range (n):
        print(j)

print_items(50)