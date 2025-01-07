# Drop non dominant time complexity: O(n^2 + n) => O(n^2)

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    
    for i in range(n):
        print(i)

print_items(50)