file_name = "employees.txt"
print("Let's open " + file_name + " file in 'append' mode.")
print("Opening...")
# modes: a - appends, w - overwrites or creates new, r+ - read and write, r - just read
employee_file = open(file_name, "a")
if employee_file.writable():
    print("File is writeable.")
    print("Appending a line...")
    employee_file.write("Toby - Human Resources\n")
else:
    print("File is not writeable.")
print("Closing file...")
employee_file.close()
print("Exiting...")
exit(0)
