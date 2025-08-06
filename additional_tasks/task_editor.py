import re
import os

with open('tasks.txt', 'r', encoding='utf-8') as file:
    all_task = file.read()

# Оновлений регулярний вираз для правильного парсингу всіх завдань
pattern = r"'''Additional task (\d+)(.*?)'''(.*?)(?='''Additional task|\Z)"

matches = re.findall(pattern, all_task, re.DOTALL)

print(f"Знайдено {len(matches)} завдань")
print("Номери знайдених завдань:", [match[0] for match in matches])

created_files = []

for match in matches:
    task_number = match[0]
    task_description = match[1].strip()
    task_code = match[2].strip()
    
    # Формуємо вміст файлу
    content = f"'''\nAdditional task {task_number}\n{task_description}\n'''\n\n{task_code}"
    
    # Створюємо файл з номером завдання
    file_name = f'{task_number}.py'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)
    
    created_files.append(file_name)
    print(f"Створено файл: {file_name}")

print(f"\nВсього створено {len(created_files)} файлів")
print("Створені файли:", created_files)

