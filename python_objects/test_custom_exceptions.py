from os import remove
from python_objects.employee import Employee, DatabaseError, MissingEmployeeError

file_name = "test_employee_file.txt"

try:
    remove(file_name)
except AssertionError:
    pass

try:
    Employee.get_all(file_name)
except Exception as err:
    assert str(err.__class__) == str(DatabaseError), f"Expected DatabaseError but got {err.__class__.__name__}"


with open(file_name, "w") as f:
    f.writelines(
        [
            "Kevin Bacon,kbacon@example.com,CEO,555-867-5309\n",
            "Bruce Wayne,bwayne@example.com,President,\n",
        ]
    )

try:
    Employee.get_at_line(3, file_name)
except Exception as err:
    assert str(err.__class__) == str(MissingEmployeeError), f"Expected MissingEmployeeError but got {err.__class__.__name__}"

new_employee = Employee("Betty White", "bwhite@example.com", "CMO", identifier=4)

try:
    new_employee.save(file_name)
except Exception as err:
    assert str(err.__class__) == str(MissingEmployeeError), f"Expected MissingEmployeeError but got {err.__class__.__name__}"
