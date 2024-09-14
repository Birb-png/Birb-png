import os
import csv
import random

output = 'Cow_Strike/pythonData'
os.makedirs(output, exist_ok=True)

path = os.path.join(output, 'Cow.csv')

def gen_random_moo(num_cows):
    colors = ['White', 'Brown']
    cows = []
    
    for _ in range(num_cows):
        cow_id = str(random.randint(10000000, 99999999))  #  8-digit ID
        color = random.choice(colors)
        age_years = random.randint(0, 10)
        age_months = random.randint(0, 11)
        
        cows.append({
            'id': cow_id,
            'color': color,
            'age_years': age_years,
            'age_months': age_months
        })
    
    return cows

num_cows = 10
cows = gen_random_moo(num_cows)

with open(path, mode='w', newline='') as file:
    fieldnames = ['id', 'color', 'age_years', 'age_months']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    for cow in cows:
        writer.writerow(cow)

print(f"Cow.csv created at: {path} with random cow data.")
