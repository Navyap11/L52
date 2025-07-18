class mmi:


    __privvar= 27;

    def __privMeth(self):
        print("I am inside class mmi")


    def hello(self):
        print("private variable value: ",mmi.__privvar)

    
a= mmi()
a.hello()
a.__privMeth

