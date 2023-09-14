#object oriented concept
#instace Variable:-Name,Amount,Address,Account Number
#Instance Methods:- CreateAccount,DisplayAccountInfo
#class Variable:-Bank name.ROI On FD
#class Method:-DisplayABankInformation
#static method:-DisplayKYCInfo


import random

class Bank_Account:
    Bank_Name="HDFC Bank PVT LTD"
    ROI_On_FD=6.7

    def __init__(self):
        self.Name=""
        self.Amount=0
        self.Address=""
        self.AccountNo=random.randint(10001,10051)
    
    def CreateAccount(self):
        print("Enter your name")
        self.Name=input()

        print("Enter your initail amount")
        self.Amount=int(input())

        print("Enter your Address")
        self.Address=input()

        
    def DisplayAccountInfo(self):
        print("..........Your account information as Below........")
        print("Name of Account Holder:",self.Name)
        print("Account Number:",self.AccountNo)
        print("Address of account Holder:",self.Address)
        print("Current Amount in Account:",self.Amount)
    
    @classmethod
    def DisplayBankInformation(cls):
        print("Wlcome to banking console")
        print("Name of Bank : ",Bank_Account.Bank_Name)
        print("Rate of Interst is {} % ".format(Bank_Account.ROI_On_FD))

    @staticmethod
    def DiplayKYCInfo():
        print("Please consider below KYC information:")
        print("According to the rules of gornverment of india tou have to submit below documents")
        print("1 : cleare and recent passport size photo")
        print("2 : photo of adar card")
        print("3 : photo of PAN  card")
    
    def Deposit(self,value):
        self.Amount=self.Amount+value
    
    def Withdraw(self,value):
        self.Amount=self.Amount-value



def main():
    print("-----------------------------------------------------")

    print("-----------Banking Application---------------")
    print("-----------------------------------------------------")

    print("-------calling static method to diplay kyc info-----------")
    print("-----------------------------------------------------")


    Bank_Account.DiplayKYCInfo()
    print("-----------------------------------------------------")


    print("------------Accesing the class varibles-----------------")

    print("-----------------------------------------------------")


    print("Name of Bank :",Bank_Account.Bank_Name)
    print("Rate of inetrest on FD is {} %:".format(Bank_Account.ROI_On_FD))

    print("-----------------------------------------------------")
 

    print("...............Accesing the class method.................")

    print("-----------------------------------------------------")


    Bank_Account.DisplayBankInformation()

    print("-----------------------------------------------------")


    print("................creting obect of class.....................")

    print("-----------------------------------------------------")



    User1=Bank_Account()
    User2=Bank_Account()

    print("-----------------------------------------------------")


    print("Creating the first account")
    print("-------------------Enter deatils for first account holder--------------")

    print("-----------------------------------------------------")


    User1.CreateAccount()

    print()

   

    print("Creating the Second account")
    print("-------------------Enter deatils for second account holder--------------")
    print("-----------------------------------------------------")


    

    User2.CreateAccount()
    print()


    print("-------------calling instance method for diplsy information---------------------")

    User2.DisplayAccountInfo()
    User1.DisplayAccountInfo()

    print("-----------------------------------------------------")



    
    print("------Deposit 500 in User1--------")
    User1.Deposit(500)

    print("------Deposit 1200 in User2--------")
    User2.Deposit(1200)


    
    print("Ammount of {} after deposit is {}".format(User1.Name,User1.Amount))
    print("Ammount of {} after deposit is {}".format(User2.Name,User2.Amount))
    
    print("-----------------------------------------------------")


    print("------withdrwa 200 in User1--------")
    User1.Withdraw(200)

    print("------withdrwa 3000 in User2--------")
    User2.Withdraw(3000)


    print("Ammount of {} after withdraw is {}".format(User1.Name,User1.Amount))
    print("Ammount of {} after withdrwa is {}".format(User2.Name,User2.Amount))



    print("----------End of application------------")

    print("-----------------------------------------------------")







if __name__ == "__main__":
    main()
