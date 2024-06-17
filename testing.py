import pyo3_smd_example

person = pyo3_smd_example.Person()
print(person)
print(f"{person.__dict__=}")
print(f"{person.address.__dict__=}")
print(f"{person.name=}")
print(f"{person.address.country=}")