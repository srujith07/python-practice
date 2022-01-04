# ATM operations:  deposite() balEnquiry() withdraw() validation()

class ATM:
    bal=10000
    def withdraw(self):
        amt=int(input("Enter withdraw amount"))      #3 times
        if amt%100==0:
            if amt<=20000:
                if amt<=self.bal-500:
                    
                    self.bal=self.bal-amt;
                else:
                    print("Please maintain minimum bal")
            else:
                print("Transaction limit is 20000 only")
        else:
            print("Please enter valid amount")
        print("avaiable bal : ",self.bal)
                
                     
                
    
    
    def deposite(self):
        amt=int(input("Enter deposite amount"))
        if amt%100==0:
            if amt<=50000:
                self.bal=self.bal+amt;
            else:
                print("Transaction limit is 50000")
        else:
            print("Please enter multiple of 100 only")
        print("avaiable bal : ",self.bal)
        
    def viewOptions(self):
        
        print("1. Deposite")      # validation
        print("2. withdraw")        
        print("3. balEnquiry")
        print("0. EXIT")
        option=int(input("Choose your option"))
        if option==1:
            obj.deposite();
            obj.viewOptions()
        elif option==2:
            obj.withdraw();
            obj.viewOptions()
        elif option==3:
             print("avaiable bal : ",self.bal)
             obj.viewOptions()
        elif option==0:
            print("Thank you, Visit again");
        else:
            print("Invalid option")
            
        
    
    def validation(self):
        pin=int(input("Enter pin "))
        if pin==1234:
            obj.viewOptions();
        else:
            print("Invalid pin")



obj=ATM();
obj.validation()