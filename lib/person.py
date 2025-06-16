# lib/person.py

class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production",
        "Legal", "Finance", "Sales", "General Management",
        "Research & Development", "Marketing", "Purchasing"
    ]

    def __init__(self, name="Unknown", job="Sales"):
        self._name = None
        self._job = None

        # Only print name if it's not the default
        if name != "Unknown":
            if isinstance(name, str) and 1 <= len(name) <= 25:
                name = name.title()
                print(f"Setting name to {name}.")
                self._name = name
            else:
                print("Name must be string between 1 and 25 characters.")
                return
        else:
            self._name = name  # silently accept default

        if job in Person.approved_jobs:
            print(f"Setting job to {job}.")
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            name = name.title()
            print(f"Setting name to {name}.")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        print("Retrieving job.")
        return self._job

    def set_job(self, job):
        if job in Person.approved_jobs:
            print(f"Setting job to {job}.")
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)
