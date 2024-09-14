import csv
import random
"""
MilkAnalyze.py (Model)
- จัดการกับข้อมูล

: Main Function:
- Cow: คลาสที่แทนวัวหนึ่งตัว รวมถึงข้อมูล เช่น ID, สี, อายุ, จำนวนขวดนมที่ผลิต, และสถานะ BSOD
- load_cows(filename): โหลดข้อมูลวัวจากไฟล์ CSV และสร้างดิกชันนารีของวัว
- search_cow(cows, cow_id): ค้นหาวัวตาม ID และตรวจสอบสถานะ BSOD
- milk_cow(cow, add_lemon): รีดนมวัวตามสีและอายุ ซึ่งอาจทำให้วัวเข้าสู่สถานะ BSOD ได้
- generate_report(cows): สร้าง report รวมถึงจำนวนขวดนมที่ผลิตและวัวที่มีสถานะ BSOD
- reset_BSOD_cows(cows): reset สถานะ BSOD ของวัว
"""
class Cow:
    def __init__(self, cow_id, color, age_years, age_months):
        self.cow_id = cow_id
        self.color = color
        self.age_years = age_years
        self.age_months = age_months
        self.milk_count = 0
        self.bsod = False

def load_cows(filename):
    cows = {}
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cow = Cow(row['id'], row['color'], int(row['age_years']), int(row['age_months']))
            cows[cow.cow_id] = cow
    return cows

def search_cow(cows, cow_id):
    if not cow_id.isdigit() or len(cow_id) != 8 or cow_id[0] == '0':
        return "Invalid ID"
    cow = cows.get(cow_id)
    if cow:
        if cow.bsod:
            return "BSOD"
        return cow
    else:
        return "Not Found"

def milk_cow(cow):
    if cow.color == 'White':# white 
        if random.random() < 0.005 * (cow.age_years * 12 + cow.age_months):
            cow.bsod = True
            return "Soy Milk (BSOD)"
        else:
            cow.milk_count += 1
            return "Regular Milk"
    elif cow.color == 'Brown':
        if random.random() < 0.01 * cow.age_years:
            cow.bsod = True
            return "Almond Milk (BSOD)"
        else:
            cow.milk_count += 1
            return "Chocolate Milk"
    else:
        return "Unknown Milk Type"

def generate_report(cows):
    report = {"Regular Milk": 0, "Sour Milk": 0, "Chocolate Milk": 0}
    bsod_cows = []
    
    for cow in cows.values():
        if cow.bsod:
            bsod_cows.append(cow.cow_id)
        elif cow.color == 'White':
            report["Sour Milk"] += cow.milk_count
        elif cow.color == 'Brown':
            report["Chocolate Milk"] += cow.milk_count
            
    total_milk = sum(report.values())
    
    return report, bsod_cows

def reset_BSOD_cows(cows):
    for cow in cows.values():
        if cow.bsod:
            cow.bsod = False
            cow.milk_count = 0
