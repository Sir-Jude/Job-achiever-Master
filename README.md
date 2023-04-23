# AI PROJECT
- For the next 2 weeks, in the afternoon you will be
working on this project in your group.
- use ai (openai for example, with the code I provided as inspiration)
create something unique
- each day I will give you an additional task to include into your program (based on that days lecture)
- YOUR OPENAI KEY: 

## little reminder
- collaborate on the work using github & board
- create a presentation for next week!

## AI PROJECT - ADDITIONAL TASK
- include some sort of stubbing in one of your unittests
- OPTIONAL: include some sort of mocking  
---


## Email sender
In this code we are going to use a **gmail** account, but the concepts apply to any other email server provider.

### 1. Create and log into a gmail account
 - create a throwaway gmail account (to be used for testing)
 - log in the new account
 - go to the setting page of your [google account](https://www.myaccount.google.com)

 ### 2. Allow the 2-Steps Veriication
 - click on "Security" (on the left)
 - Scroll to the section "Signing in to Google"
 - click on "2-Steps Verification"
 - follow the instructions on the screen

### 3. Create an app password
 - go to the link fro creating an [app password](https://myaccount.google.com/u/4/apppasswords)
 - click on the first dropdown menu7
 - Select "Other (Custom name)"
 - choose a name (for example "Python")
 - copy the 16 character app password in the yellow box

 ## 4. Import the necessary modules
 - **EmailMessage**  
   This is a class of the *email.message* module (submodule of *email* package) and creates an email object, which sets its object, body and sender/receiver's address.
 - **SMTP_SSL**  
   This is a class of the module smtplib (Simple Mail Transfer Protocol LIBrary) and takes care of sending the email
 - **ssl** module.  
   This encrypts the connection and makes sure both the login credentials and message are not easily accessed by others.

## 5. Create an object email and fill the necessary fields
 - Write an assignment statement for the:
    - credentials (email and password) to login into the gmail account
    - receiver's email
    - subject
    - body
 - Initiate the EmailMessage's object.
 - Assign te above created variables to the EmailMessage **dictionary**'s correct key: the conceptual model provided by an EmailMessage object is that of an ordered dictionary (indexed by the header names, such as "from", for the email sender, "to" for the email receiver, etc...) coupled with the body of the email assigned to the method **set_content**.

 ## 6. Encrypet the email
 Write an assignment statement and use the ssl method **create_default_context** to protect the details of the email (sender/receiver address and message)

 ## 7. Send the email
 - Initiate a "SMTP_SSL" class object, which requires three attributes:
   1. the email server (for gmail)
   2. the port (for gmail)
   3. the SSL protocol
 - Call a "with" statment to parse the above details
 - Call SMTP_SSL method "login", which require 2 arguments:
   1. the email of the sender
   2. password
 - Send the message with the SMTP_SSL method "sendmail", which requires 3 arguments:
   1. the email of the sender
   2. the email of the receiver
   3. the em object, formatted with the EmailMessage method "as_string()"

 ### References:
 - Python docs: [**email** package](https://docs.python.org/3/library/email.html)
 - YouTube :["How to Send Emails with Python"](https://www.youtube.com/watch?v=g_j6ILT-X0k&ab_channel=ThePyCoach)
 ---