dog = dict()
dog = {"name": "luky", "color": "cafe", "breed": "pastor aleman", "legs": 4, "age": 2}
student_dictionary = {
    "first_name": "Angel",
    "last_name": "Tiscareño",
    "gender": "Masculino",
    "age": 18,
    "marital_status": "soltero",
    "skills": ["jugar beisbol"],
    "country": "Mexico",
    "city": "Aguascalientes",
    "address": "240645",
}
print(len(student_dictionary))
print(student_dictionary["skills"])
print(type(student_dictionary["skills"]))
student_dictionary["skills"].append("jugar basquetball")
list_keys = list(student_dictionary.keys())
list_values = list(student_dictionary.values())
list_of_tuples = [(k, v) for k, v in student_dictionary.items()]
student_dictionary.pop("marital_status")
del dog