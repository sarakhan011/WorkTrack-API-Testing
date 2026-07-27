CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL,
    ManagerID INT,
    FOREIGN KEY (ManagerID)
        REFERENCES Employees(EmployeeID)
);

ALTER TABLE Employees
ADD CONSTRAINT Employee_Department
FOREIGN KEY (DepartmentID)
REFERENCES Departments(DepartmentID);