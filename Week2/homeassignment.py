# Date: 31st July 2023
# Create an XML file named "employees.xml" with information about two employees. Use the ElementTree module to build an XML tree, define elements, set attributes, and write the XML content to a file.

import xml.etree.ElementTree as ET

def create_employee_element(employee_data):
    employee = ET.Element('employee')
    for key, value in employee_data.items():
        employee.set(key, str(value))
    return employee

# Employee data
emp1_data = {
    'id': 1,
    'name': 'Rahul',
    'position': 'HR Manager'
}

emp2_data = {
    'id': 2,
    'name': 'Rohan',
    'position': 'Data Scientist'
}

# Create the root element
emp = ET.Element('employees')

# Create employee elements and add them to the root element
emp1 = create_employee_element(emp1_data)
emp2 = create_employee_element(emp2_data)

emp.append(emp1)
emp.append(emp2)

# Create the ElementTree
tree = ET.ElementTree(emp)

# Write the XML content to a file
with open('Syllabus/Week2/employees.xml', 'wb') as file: # wb => Binary Write mode
    tree.write(file, encoding='utf-8', xml_declaration=True)

print("employees.xml created successfully.")
