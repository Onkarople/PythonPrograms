import time

def DispalyEven(No):
    for i in range(1,No+1):
        if(i%2==0):
            print("Even Number:",i)
    



def DisplayOdd(No):
    for i in range(1,No+1):
        if(i%2!=0):
            print("Odd Number:",i)
    




def main():
    print("demonstration of serial programming")
    DispalyEven(2000)
    print()
    DisplayOdd(2000)

if __name__ == "__main__":
    start_time=time.time()
    main()
    end_time=time.time()
    print("Excution Time is:",end_time-start_time)