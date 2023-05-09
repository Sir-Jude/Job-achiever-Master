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
![Email internet path](email.png)

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
- click on the first dropdown menu ("select app")
- Select "Other (Custom name)"
- choose a name (for example "Python")
- click on "Generate"
- copy the 16 character app password in the yellow box  
**IMPORTANT**: This is the **one and only time** you will be able to see this, so copy and paste it in a separate and safe location.

## 4. Import the necessary libraries  
- **SMTP**  
  A class of the module smtplib (Simple Mail Transfer Protocol LIBrary) and takes care of sending the email.
- **MIMEMultipart**  
  A subclass of MIMEBase, this is an intermediate base class for MIME messages that are not multipart. The primary purpose of this class is to prevent the use of the attach() method, which only makes sense for multipart messages.
- **MIMEApplication**  
  A subclass of MIMENonMultipart, this class is used to represent MIME message objects of major type application. The _data  argument contains the bytes for the raw application data while the optional _subtype specifies the MIME subtype.
- **MIMEText**  
  A subclass of MIMENonMultipart, the MIMEText class is used to create **MIME** (**M**ultipurpose **I**nternet **M**ail **E**xtension) objects of major type text.


## 5. Set to up the server and the port
- Write an assignment statement for the:
  - SMTP server  
    (we are using tho one for gmail, but it is possible to use anyone else)
  - port  
    (**587** is the the standard secure mail submission port.)

## 6. Set up the credentials to log into the email account  
- write an assignment statement for the sender's email
- use a "with" statement and the "open" function in "r" (read) mode to access the file where the app password is stored.

## 7. Set up all the other email details
- list of receivers
- subject

## 8. Attach the document(s)
- Open and read the file in binary mode to attach an image







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
 - Python docs:  
    - [**smtplib** module](https://docs.python.org/3/library/smtplib.html#module-smtplib)
    - [**email.mime** module](https://docs.python.org/3/library/email.mime.html?highlight=email#email.mime.multipart.MIMEMultipart)
  - Port number details [**"Which SMTP port should I use?"**](https://www.mailgun.com/blog/email/which-smtp-port-understanding-ports-25-465-587/)
 ---


 ## User Input
 The **user_input.py** file contains a 'User' class. The class gathers user information including: Name, Age, Email, Phone Number, Work Experience and Education.

 To use this class you need to instantiate an object of the class and then call its **get_info()** method to get all the user info, then to display the user info call the **print_info()** method.
 




- [**E-mail regex** link](https://uibakery.io/regex-library/email-regex-python)

