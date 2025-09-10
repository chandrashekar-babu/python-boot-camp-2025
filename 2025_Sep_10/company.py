staff = set()

founding_members = {"Alice", "Bob", "Charlie"}
staff.update(founding_members)

def hire(name):
    staff.add(name)
    print(f"Hired {name}")

def fire(name):
    if name in founding_members:
        print(f"Cannot fire founding member {name}")
    else:
        staff.remove(name)
        print(f"Fired {name}")

def list_staff():
    print("Current staff:")
    for member in staff:
        print(f"- {member}")
