# import random
# names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]
#
# students_score = {student:random.randint(1,100) for student in names}
# print(students_score)
#
# passed_students = {student:score for (student, score) in students_score.items() if score >= 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: (weather_c * 9/5) + 32 for day, weather_c in weather_c.items()}
print(weather_f)

# (temp_c * 9/5) + 32 = temp_f