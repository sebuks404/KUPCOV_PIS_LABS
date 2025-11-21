groupmates = [
    {
        "name": "Себастиан",
        "surname": "Купцов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [4, 2, 3]
    }
]

for student in groupmates:
    avg_mark = sum(student["marks"]) / len(student["marks"])
    print(f"{student['name']} {student['surname']}: средний балл {avg_mark:.2f}")

all_marks = [mark for student in groupmates for mark in student["marks"]]
overall_avg = sum(all_marks) / len(all_marks)
print(f"\nСредний балл всех учеников: {overall_avg:.2f}")