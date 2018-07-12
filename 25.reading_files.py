file_name = "employees.txt"
print("Let's open " + file_name + " file.")
print("Opening...")
employee_file = open(file_name, "r")
if employee_file.readable():
    print("File is readable.")
    print("------ File: ------")
    # print(employee_file.read())  # Reads and displays entire file.
    # print(employee_file.readline())  # Read one line
    # print(employee_file.readlines())  # Read all lines into array and display it.
    # print(employee_file.readlines()[0])  # Read all lines and display first line.
    for employee in employee_file.readlines():
        print(employee.strip())  # Using strip() to strip new line character at the end of lines.
    print("--- End of File ---")
else:
    print("File is not readable.")
print("Closing file...")
employee_file.close()
print("Exiting...")
exit(0)
