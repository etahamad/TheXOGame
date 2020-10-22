import time


#our function for counting from 0-20
def counting():
    for i in range(0,21):
        if i==20:
            print("counting at: "+str(i))
            print("Done counting...")
        else:
            print("counting at: "+str(i))
            time.sleep(5) #sleep for 5 seconds

#our main function
if __name__ == '__main__':
    counting() #call our counting method