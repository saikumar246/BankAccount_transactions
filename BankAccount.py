
list_of_transactions=[]
def read_data(list):
    for i in range(len(list)):
        list[i]=list[i].split(":")
    list_of_transactions=list

def display_list(list):
    print("List of transactions")
    print("Date        Type           Amount")
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    for i in range(len(list)):
        for j in range(3):
            print(list[i][j],end="    ")
        print("\n")
    print("\nEnd of the list")

def new_transaction(list):
    date=input("enter the date of transcationin the format(yyyymmdd):")
    date='\n'+date
    transaction_type=str(input("Enter the transaction type from the options(Deposit\tWithdraw\tBank charge\tinterest)"))
    amount=str(input("Enter the amount:"))
    list.append([date,transaction_type,amount])
    list_of_transactions=list


def current_balance(list):
    curr_amt=0
    for i in range(len(list)):
        for j in range(3):
            if list[i][j]=="deposit":
                t=str(list[i][j+1])
                if t[-1]=="\n":
                    curr_amt+=float(t[:-1])
                else:
                    curr_amt += float(t)
            elif list[i][j]=="withdraw":
                t = list[i][j + 1]
                if t[-1]=="\n":
                    curr_amt -= float(t[:-1])
                else:
                    curr_amt -= float(t)
            elif list[i][j]=="bank charge":
                t = list[i][j + 1]
                if t[-1] == "\n":
                    curr_amt -= float(t[:-1])
                else:
                    curr_amt -= float(t)
            elif list[i][j]=="interest":
                t = list[i][j + 1]
                if t[-1] == "\n":
                    curr_amt += float(t[:-1])
                else:
                    curr_amt += float(t)
                continue
    return curr_amt
def save_data(list):
    fp=open("bank_account_data.txt","w")
    for i in range(len(list)):
        list[i]=':'.join(list[i])
    #print(list)
    fp.writelines(list)
def main():
    print("Welcome to Bank Accout Application")
    while 1:

        print("\n-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("A - Read data from the file\nB - Display list of transactions\nC - Add a new transaction\nD - Calculate current balance\nE - Save data to a file\nQ - Quit")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        choice=str(input("Please select an option by typing A,B,C,D,E or Q?"))
        if((choice=="A") or (choice=="a")):
            fp=open("bank_account_data.txt","r")
            list_of_transactions = fp.readlines()
            read_data(list_of_transactions)
        elif(choice=="B" or choice=="b"):
            print("display the transactions")
            display_list(list_of_transactions)
        elif(choice=="C" or choice=="c"):
            new_transaction(list_of_transactions)
        elif(choice=="D" or choice=="d"):
            current=current_balance(list_of_transactions)
            print("current amount:",current)
        elif(choice=="E" or choice=="e"):
            save_data(list_of_transactions)
            print("save data")
        elif(choice=="Q" or choice=="q"):
            quit()
        else:
            print("Incorrect action type, Please try again")
    print("Thanks for using Bank account Application")

    #t1=Transaction(20201105,"deposit",1000.00)
    #t1.display()


if __name__=="__main__":
    main()