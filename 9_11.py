from imported_admin import Admin

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
