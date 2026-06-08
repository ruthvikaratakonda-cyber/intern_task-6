class EmployeeRepository:

    def get_by_id(
        self,
        employee_id,
        db
    ):

        return db.query(Employee).filter(
            Employee.id == employee_id
        ).first()