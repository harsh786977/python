import pywhatkit    
import random       
import pyautogui as pg    
import time
import pywhatkit as pwk

# import ktp.sendwhatmsg_image as kt  (Not official package) #need to install

#function that works under the wbot1 (function)
def w1():
             quit=input("Are you sure you want to exit...>>>\n")
             if (quit=='yes','y','Y'):
                  exit()
             elif (quit=='no',"n","N"):
                print("Welcome back to the whatsapp bot__>>\n")
                wbot1() 
                
# Function to send automated WhatsApp message
def wbot1():
    try:
        # Taking user input for phone number, message, and scheduled time
        phn_no = input("Enter the phone number with country code... :")
        msg = input("Enter The message you want to send... :")
        h = int(input("Enter the time in hours :"))
        m = int(input("Enter the time in minutes :"))

        # Sending WhatsApp message using pywhatkit
        pywhatkit.sendwhatmsg(phn_no, msg, h, m)

         #Delay before closing whatsapp
        time.sleep(5)
        
        #auto closing whatsapp in 5 seconds.
        pg.hotkey('alt', 'f4') 

        # Closing WhatsApp after sending all the messages
          ####### use to auto close whatsapp  
        print("Message sent successfully!")

         # To send another message
        print("Do You want to continue with another person... ")
        ans=input("Press Y/N according to your choice / Press 0 to exit :")
        if (ans=="yes",'y','Y'):
            wbot1()
        if (ans=="no","n","N"):
            auto()  
        if (ans=='0'):
            w1()

    except Exception as e:
        print("ERROR OCCURED :", str(e))
        wbot1()

#function that works under the wbot2 (function)
def w2():
             quit=input("Are you sure you want to exit...>>>\n")
             if (quit=='yes'):
                  exit()
             elif (quit=='no',"n","N"):
                print("Welcome back to the whatsapp bot__>>\n")
                wbot2() 
                
# Function for an automated message sending bot
def wbot2():
    try:
       ###################### #List needed ###################################################
         #some names 
        animal=('kidda','lodu','taran lul')
        
        #number of messages want to send.
        m=int(input("Enter the amount of messages you want to send--->>"))
        
        #delay of 8 seconds to click on the chat
        time.sleep(8)

        #using loop to send random multiple messages
        for i in range(m):
            a=random.choice(animal)
            pg.write("hello "+a)
            pg.press('enter')
            
            #Delay before closing whatsapp
            #time.sleep(5)
            #pg.hotkey('alt', 'f4')
           

            # Closing WhatsApp after sending all the messages
         ####### use to auto close whatsapp   pg.hotkey('alt', 'f4')
            print("Message sent successfully!")

                  # To send another message
        print("Do You want to continue with another Person... ")
        ans=input("Press Y/N according to your choice / Press 0 to exit:")
        if (ans=="y",'y','Y'):
            wbot2()
        if (ans=="n","n","N"):
            auto()  
        if (ans=='0'):
            w2()
            
    except Exception as e:
     print(f"An error occurred: {e}")
     wbot2()    


########   UNDER WORK UNABLE TO INSTALL KTP.WHATSIMAGE PACKAGE (NOT OFFICIAL LIBRARY ) #################

#function that works under the wbot2 (function)
def w3():
             quit=input("Are you sure you want to exit...>>>\n")
             if (quit=='yes','y','Y'):
                  exit()
             elif (quit=='no',"n","N"):
                print("Welcome back to the whatsapp bot__>>\n")
                wbot3() 
                
#function to send file etc... 
def wbot3():
    try:
         # Send a message with an image
        ph = input("Enter the phone number with country code... :")
        msg = input("Enter The message you want to send... :")
        file_path = input("Enter the path of the file you want to send :")
        h = int(input("Enter the time in hours :"))
        m = int(input("Enter the time in minutes :"))
        pwk.sendwhatmsg(ph, msg, file_path, h, m)

        # Closing WhatsApp after sending all the messages
        pg.hotkey('alt', 'f4')
        
                   # To send another message
        print("Do You want to continue with another Person... ")
        ans=input("Press Y/N according to your choice / Press 0 to exit:")
        if (ans=="yes",'y','Y'):
            wbot3()
        if (ans=="no","n","N"):
            auto()  
        if (ans=='0'):
            w3()
            
    except Exception as e:
     print(f"An error occurred: {e}")
     wbot3()      

########   UNDER WORK UNABLE TO INSTALL KTP.WHATSIMAGE PACKAGE (NOT OFFICIAL LIBRARY ) #################  

#function that works under the auto (function)
def a():
             quit=input("Are you sure you want to exit...>>>\n")
             if (quit=='yes','y','Y'):
                  exit()
             elif (quit=='no',"n","N"):
                print("Welcome back to the whatsapp bot__>>\n")
                auto() 
                
# Function to choose and execute the desired bot
def auto():
    try:
        # Taking user input for the bot to use
        a = input("Choose the Bot you want to use___>>\nPress 1 for Automated WhatsApp Message___>\nPress 2 for Multiple Automated Message___>\n--->>")

        # Checking user choice and calling the appropriate function
        if (a == '1'):
            wbot1()
            
        elif (a == '2'):
            wbot2()

            #### UNDER WORK #### 
        elif a == '3':
            wbot3()
                #### UNDER WORK ####
        else:
            print("Invalid Choice! Try Again.")
            auto()
    except Exception as e:
        print("Error occurred:", str(e))
        auto()
auto()