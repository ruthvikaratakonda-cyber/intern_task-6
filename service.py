class EmployeeService:

    def create_employee(
        self,
        employee_data,
        db
    ):

        employee = Employee(
            **employee_data
        )

        db.add(employee)
        db.commit()

        return employee