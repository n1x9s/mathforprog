import matplotlib.pyplot as plt

num_categories = int(input("Введите количество категорий: "))
categories = []
sales = []

for i in range(num_categories):
    category = input(f"Введите название категории {i+1}: ")
    sale = float(input(f"Введите продажи для категории {category}: "))
    categories.append(category)
    sales.append(sale)

plt.figure(figsize=(8, 8))
plt.pie(sales, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Процентное соотношение продаж по категориям')
plt.show()