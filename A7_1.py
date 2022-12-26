import threading as td

class odd_even_thread:
     
     def __init__(self,No):
          self.No=No
          
     def even(self):
          print("Even No is: ",end=" ")
          for i in range(2,self.No+1):
               if(i%2==0):
                    print(i,end=" ")
               
          print("")
          
     def odd(self):
          print("Odd No is: ",end=" ")
          for i in range(2,self.No+1):
               if(i%2!=0):print(i,end=" ")
          print("")
     
def main():
     No=int(input("Enter No : "))
     nObj1 =odd_even_thread(No)
     t1=td.Thread(target=nObj1.even,args="")
     t2=td.Thread(target=nObj1.odd,args="")
     t1.start()
     t1.join()
     t2.start()
     t2.join()
     
if __name__ =="__main__":
     main()
     
     
     
          
     