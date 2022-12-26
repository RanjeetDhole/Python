import threading as td

class odd_even_thread:
     def __init__(self,No):
          self.No=No
          
     def even(self,No):
          print("Even Factor of sum is: ",end=" ")
          sum = 0
          
          for i in range(2,No):
               if(i%2==0 and No%i==0):
                    sum+=i 
          print(" ",sum)
          
     def odd(self,No):
          print("Odd Factor of sum is: ",end=" ")
          sum = 0
          for i in range(2,No):
               if(i%2!=0 and No%i==0):
                    sum+=i
          print(" ",sum)
     
def main():
     No=int(input("Enter No : "))
     nObj1 =odd_even_thread(No)
     t1=td.Thread(target=nObj1.even,args=(No))
     t2=td.Thread(target=nObj1.odd,args=(No,))
     t1.start()
     t1.join()
     t2.start()
     t2.join()
     
if __name__ =="__main__":
     main()
     
     
     
          
     