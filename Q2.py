n = int(input())
students = []
for _ in range(n):
    st = input()
    grade = float(input())
    students.append([st, grade])
students = sorted(students, key=lambda x: x[1])
twoMin = 0
minGrade = students[0][1]
namelist = []
for i, (name, grade) in enumerate(students[1:]):
        if grade == minGrade:
            continue
        if not twoMin:
            twoMin = grade
            namelist.append(name)
            continue
        if grade == twoMin:
            namelist.append(name)
        else:
            break
namelist.sort()
for name in namelist:
    print(name)
