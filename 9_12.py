# Store the User class in one module, and store the Privileges and Admin,
# Classes in a separate module. In this file create an Admin instance and call,
# show_privileges() to show the everything works correctly.
from imported_admin_3 import Admin

jon = Admin('jon', 'doe', 'tokyo', '25', 'male')
jon.describe_user()

jon.privileges.show_privileges()

print("\nAdding privileges...")
jon_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
jon.privileges.privileges = jon_privileges
jon.privileges.show_privileges()
