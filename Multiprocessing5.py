import time
import multiprocessing

def DisplayEven(No):
    for i in range(1,No,1):
        if(i % 2 == 0):
            print("Even number : ",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if(i % 2 != 0):
            print("Odd number : ",i)

def main():
    print("Demonstartion of parallel programming using multiple process")
    Number = 20000000000
    p1 = multiprocessing.Process(target = DisplayEven,args = (Number,))
    p2 = multiprocessing.Process(target = DisplayOdd,args = (Number,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("End OF Main")
     
if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)