students = ["Juan", "María", "Pedro"]

database = [["Juan", [6.4, 7.0, 9.1]],
            ["María", [8.2, 9.8, 6.5]],
            ["Pedro", [7.1, 8.4, 5,2]]
            ]
student_av = []


for student in database:
    #student_av.append([student[0], round(sum(student[1])/len(student[1]), 2)])
    student_av.append(round(sum(student[1])/len(student[1]), 2))

class_av = round(sum(student_av)/len(student_av), 2)
print("La nota media de los estudiantes es: ")


for i in range(0,len(students)):
    print(f"La nota de {students[i]} es {student_av[i]}")
print(f"La nota media de la clase es: {class_av}")