#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", job="Unknown"):
        self.name = name
        self.job = job

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name (validates and formats)
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()  # Convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # Getter for job
    def get_job(self):
        return self._job

    # Setter for job (validates job)
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)


# Test code (optional)
if __name__ == "__main__":
    person1 = Person("john doe", "ITC")
    print(f"Person's name: {person1.name}, Job: {person1.job}")

    person2 = Person("verylongnamethatiswaytoolong", "Sales")  # Invalid name
    person3 = Person("Alice", "UnapprovedJob")  # Invalid job
