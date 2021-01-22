from collections import defaultdict


# hackerrank problem's:
# In this challenge, you will be given  integers n  and m
# There are n words, which might repeat, in word group A
# There are m words belonging to word group B
# For each  words, check whether the word has appeared in group A or not.
# Print the indices of each occurrence of m in group A
# If it does not appear, print -1

dd = defaultdict(list)  # default_factory is []
n, m = map(int, input().strip().split())

for i in range(1, n + 1):
    word = input()
    dd[word].append(str(i))

for i in range(m):
    word = input()
    print(" ".join(dd[word]) or -1)


# defaultdict for counting letters in string (counting values)
s = "misssisssgissaaaddssd"

dd_i = defaultdict(int)  # set to int, default_factory is initialize to 0
for letter in s:
    dd[letter] += 1

dd_i

# defaultdict for grouping items
dd_l = defaultdict(list)  # default_factory is set to []
dep = [
    ("Sales", "John Doe"),
    ("Sales", "Martin Smith"),
    ("Accounting", "Jane Doe"),
    ("Marketing", "Elizabeth Smith"),
    ("Internal Audit", "Ng Hoai Diem Tram"),
    ("Tech", "Pham Ng Xuan Hoa"),
    ("Data Analyst", "Tran Viet Phuoc"),
]

for department, employee in dep:
    dd_l[department].append(employee)

dd_l

# Accumulating values
incomes = [
    ("Books", 1250.00),
    ("Books", 1300.00),
    ("Books", 1420.00),
    ("Tutorials", 560.00),
    ("Tutorials", 630.00),
    ("Tutorials", 750.00),
    ("Courses", 2500.00),
    ("Courses", 2430.00),
    ("Courses", 2750.00),
]
dd_f = defaultdict(float)  # default_factory to 0.0
for product, income in incomes:
    dd_f[product] += income

for product, income in dd_f.items():
    print(f"Total income for {product}: ${income:,.2f}")


# defaultdict deep dive
