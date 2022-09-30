class Employee:
    def __init__(self, name, IDnumber, department, job_title, monthly_salary):
         self.__name = name
         self.__IDnumber = IDnumber 
         self.__department = department
         self.__job_title = job_title
         self.__monthly_salary = monthly_salary

    def getname (self):
        return self.__name
    
    def getIDnumber (self):
        return self.__IDnumber

    def getdepartment (self):
        return self.__department
    
    def getjob_title (self):
        return self.__job_title
    
    def getmonthly_salary (self):
        return self.__monthly_salary
