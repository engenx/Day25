import csv
import pandas

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    print(data)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)

# with open('weather_data.csv', 'r') as f_in, open('weather_data.txt', 'w') as f_out:
#     # 2. Read the CSV file and store in variable
#     weather = f_in.readlines()
#     # 3. Write the content into the TXT file
#     for items in weather:
#         weather = items.strip()
#         f_out.write(weather)
#
#     # with open("./Input/Letters/starting_letter.txt") as letter_file:
#     #     letter_contents = letter_file.read()
#     #     for name in names:
#     #         fresh_name = name.strip()
#     #         new_letter = letter_contents.replace(PLACEHOLDER, fresh_name)
#     #         with open(f"./Output/ReadyToSend/letter_for_{fresh_name}.txt", mode="w") as completed_letter:
#     #             completed_letter.write(new_letter)