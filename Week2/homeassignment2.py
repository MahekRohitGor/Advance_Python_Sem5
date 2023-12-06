# Date: 1st August 2023
# There exists four different files, each contains Individual Student's  name, id_no, branch and achievement. Combine the data of these 4 students into the Achievement.txt file

import csv

# List to store combined data
combined_data = []

# List of file names for individual students
student_files = ["Syllabus/Week2/student1.csv", "Syllabus/Week2/student2.csv", "Syllabus/Week2/student3.csv", "Syllabus/Week2/student4.csv"]

# Read data from individual student files
for file_name in student_files:
    with open(file_name, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            combined_data.append(row)

# Write the combined data to Achievement.txt
output_file = "Syllabus/Week2/Achievement.txt"
with open(output_file, 'w', newline='') as file:
    fieldnames = ["name", "id_no", "branch", "achievement"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Write header row
    for data in combined_data:
        writer.writerow(data)

print(f"Data of {len(combined_data)} students combined and written to '{output_file}'.")
