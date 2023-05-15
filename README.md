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

## Cover letter bot

The bot takes the User info from the candidate.json file and the job info from the job.json file. It then creates
a cover letter using all the information. Once the cover letter is generated, the user has the option to edit the generated text
via the tkinter module. When you close the tkinter window, the program then automatically saves the Cover letter as pdf, a new tkinter
window appears where the user can choose the path to save the pdf file.

---
## Email module

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
- click on the first dropdown menu ("select app")
- Select "Other (Custom name)"
- choose a name (for example "Python")
- click on "Generate"
- copy the 16 character app password in the yellow box  
**IMPORTANT**: This is the **one and only time** you will be able to see this, so copy and paste it in a separate and safe location.

### 4. Import the necessary libraries  
- **SMTP**  
  A class of the module smtplib (Simple Mail Transfer Protocol LIBrary), it takes care of conecting to the server and sending the email.
- **MIMEMultipart**  
  A subclass of MIMEBase, this class represents the outer container of an email message and allows to combine different components ("multipart"), such as sender and receiver address, subject, body and attachments into a single email message.
- **MIMEApplication**  
  A subclass of MIMENonMultipart, this class is used to represent MIME message objects of major type application. The _data  argument contains the bytes for the raw application data while the optional _subtype specifies the MIME subtype.
- **MIMEText**  
  A subclass of MIMENonMultipart, the MIMEText class is used to create **MIME** (**M**ultipurpose **I**nternet **M**ail **E**xtension) objects of major type text.

### 5. Create the class **Email**
  - ### 5.1 define the **class attributes**
    Write an assignment statement for the port.  
    (**587** is the the standard secure mail submission port)

  - ### 5.2 Instatiate the class instance
    The class Email has the following attributes:  
    - sender
    - list of receivers
    - email subject
    - name of the server  
      (defaulted for the gmail)  

  - ### 5.3 Define **password** method
    This method uses a "with" statement and the "open" function in "r" (read) mode to access the file where the app password is stored, recover it, return to the main funcion and closing the file at the end of its scope.
  
  - ### 5.3 Define **attachments** method
    - loop through a copy of the list of documents
    - open the file containing the document.  
      **NB**: using the "**binary**" ("rb") mode instead of the simple "read" ("r") allows us to open files others than text, such as pdf or images
    - read the file and use its data to create an instance of the general-purpose class "**MIME application**", which rappresent an attachment in an email message.
    - use the **.add_header()** method to add the "Content-Disposition" header, which indicates the file should be treated as an attachment, to the attachment object
    - remove the string name of the document from the original list and substitute it with the attachment object.
    - return the new list of documents  

  - ### 5.3 Define **send** method
    - 5.3.1 Connect to the server  
      - Use a "with" statement to be sure the server will be close once we finish to send all the emails  
      - Create an object of the class SMTP, which allows the connection to the serveer using the proper server's name and standard secure SMTP port number  
      - Use the .strarttls() method to encrypt the connection
      - Use the .login() method to log into the email account with the sender address and its password.
    - 5.3.2 "Build" and send the email
      - loop through the list of the receivers
      - create an instance of the class **MIMEMultipart()**, which is like a box contaiing all the different components of the email
      - Set each needed element inside the container:
        - sender's address 
        - receiver's address
        - email subject
        - body of the email, creating an instance of the class **MIMEText** and attaching it throught the .attach() method
        - attachment(s), looping through the list of files to be attached and using the .attach() method
      - Finally, use the smtp **.send_message()** method to send the MIMEMultipart() object, which rapresent the email with all its different components.

### References:
- Python docs:  
  - [**smtplib** module](https://docs.python.org/3/library/smtplib.html#module-smtplib)
  - [**email.mime** module](https://docs.python.org/3/library/email.mime.html?highlight=email#email.mime.multipart.MIMEMultipart)
- Port number details [**"Which SMTP port should I use?"**](https://www.mailgun.com/blog/email/which-smtp-port-understanding-ports-25-465-587/)
---


## User Input
The **user_input.py** file contains a 'User' class. The class gathers user information including: Name, Age, Email, Phone Number, Work Experience and Education.

#### **get_info()**
This class collects all the user info.

#### **json_info()**
This class returns a json object containing all the info collected.

#### **dict_info()**
This class returns a dict containing all the info collected.


---
 

## References


- [**E-mail regex** link](https://uibakery.io/regex-library/email-regex-python)

