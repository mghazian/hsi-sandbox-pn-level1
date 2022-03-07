# 54:06 String Method
course = "Belajar Python Bareng Agung Setiawan"
length = len(course)
print (length)

course_capital = course.upper()
print(course_capital)

course_lowercase = course.lower()
print(course_lowercase)

print(course_lowercase.capitalize())
print(course_lowercase.title())
print(course.replace("Python", "Javascript"))

language = "Python"
print(language in course)

language = "Javascript"
print(language in course)