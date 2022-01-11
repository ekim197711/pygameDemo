

song_choice_for_each_person = {"Mike": "Disco", "Susan": "Love", "Jack": "Techo", "Henrik": "Country"}

for key in song_choice_for_each_person:
    choice = song_choice_for_each_person[key]
    print("Choice: ", choice)

print(" --- ")

for key, value in song_choice_for_each_person.items():
    print("Person: ", key, " Choice: ", value)



