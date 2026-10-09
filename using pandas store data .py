import pandas as pd

data = [
    ["sandy", 65, 78, 54, 67, 88, 352],
    ["sushma", 87, 76, 95, 47, 58, 363],
    ["varshi", 67, 55, 46, 67, 90, 325],
    ["pandu", 65, 87, 39, 84, 50, 325],
    ["tillu", 45, 73, 59, 76, 66, 319],
    ["chaitu", 56, 47, 87, 59, 49, 298]
]

columns = ["name", "tel", "hin", "eng", "maths", "science", "total"]

df = pd.DataFrame(data, columns=columns)
#print(df)


subjects = columns[1:-1]

# Top student based on total marks
top_index = df["total"].idxmax()
print("Top student:", df.loc[top_index, "name"])
print("Highest total:", df.loc[top_index, "total"])

# Highest individual subject mark
highest_by_subject = df[subjects].max()
highest_mark = highest_by_subject.max()
highest_subject = highest_by_subject.idxmax()
highest_student_index = df[highest_subject].idxmax()

print("Highest subject mark:", highest_mark)
print("Subject:", highest_subject)
print("Student:", df.loc[highest_student_index, "name"])

# Averages
print("Average total:", df["total"].mean())
print("Average marks by subject:")
print(df[subjects].mean())