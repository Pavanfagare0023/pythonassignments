# Inheritance for Manager 

class Employee:
    _empid=None
    _empname=None
    _bs=None
    _hra=None
    _da=None
    _pf=None
    _gross=None
    def __init__(self,empid,empname,bs):
        self._empid=empid
        self._empname=empname
        self._bs=bs
    def getSalary(self):
        self._hra=self._bs*0.40
        self._da=self._bs*0.30
        self._pf=self._bs*0.12
        self._gross=(self._bs+self._hra+self._da)-self._pf
        
    def __str__(self):
        return f'empid={self._empid}\nempname{self._empname}\nEmployee Salary={self._gross}'
        

e1=Employee(1,'Akshay',23000)
e1.getSalary()
print(e1)



class Manager(Employee):
    __food=None
    __ta=None
    def __init__(self,empid,empname,bs,food,ta):
        super().__init__(empid, empname, bs)
        self.__food=food
        self.__ta=ta
    #polymorphism --> method overriding    
    def getSalary(self):
        print('in manager class')
        self._hra=self._bs*0.45
        self._da=self._bs*0.25
        self._pf=self._bs*0.12
        self._gross=(self._bs+self._hra+self._da+self.__food+self.__ta)-self._pf

    def __str__(self):
        return f'empid={self._empid}\nempname{self._empname}\nManager Salary={self._gross}'


m1=Manager(2,'Amol',45000,2000,7000)
m1.getSalary()
print(m1)

    
    