<p align="center"
<img src ="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Stack_Overflow_icon.svg/768px-Stack_Overflow_icon.svg.png" width = 200px>
</p>

<h1 align = 'center'> ExpressMailer
</h1>

<p align='center'>
A Fast Mail Service based on sockets(Firebase) with all necessary features like Email, Chat, Video Conference, Spam detection, Encryption, OAuth, etc .
   <br><br>
</p>

<div align="center">

[![](https://img.shields.io/badge/Made_with-Flask-blue?style=for-the-badge&logo=Flask)](https://flask.palletsprojects.com/en/1.1.x/)
&emsp;[![](https://img.shields.io/badge/IDE-Visual_Studio_Code-red?style=for-the-badge&logo=visual-studio-code)](https://code.visualstudio.com/ "Visual Studio Code")

</div>

-----------------------------------
<h2 align='center'>Motivation</h2>
<p align='center'>
We all are completely dependent on Gmail like applications. When such services are down we face a lot of trouble, also privacy is issue of concern now-a-days. 
Thus, our project helps building single page, highly customizable and scalable mail service with complete control over privacy for an particular organization.
<br>

</p>

------------------------------------------
### Why does the application looks similar to Gmail?
<p>
  After knowing that Whatsapp was going to change it's Privacy Policies, It was expected that users would start using alternatives like Signal/Hike but that wasn't the case.
  Analyzing Signal/Hike vs Whatsapp situation, Users don't tend to accept the changes because users were used to UI they were using since long. 
  Thus, we tried to keep the UI as similar as Gmail.
 </p>
 

-----------------------------------

### 🚀 Features

<p align="left">
   <ul>
      <li>Spam mail detection using Random Forest Classifier</li>
      <li>Keyword extraction using Term Frequency – Inverse Document Frequency(TFIDF) technique</li>
   </ul>
</p>


-----------------------------------

### :guide_dog: Installation Guide

A step by step series of examples that tell you how to get a development env running

1. Clone the repo
  ```
  $ git clone https://github.com/ExpressMailer/ExpressMailer-ML.git
  $ cd ExpressMailer-ML
  ```

2. Initialize and activate a virtualenv(For Windows):
  ```
  $ pip install virtualenv
  $ virtualenv --no-site-packages env
  $ cd env/Scripts
  $ activate.bat
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

4. Run the development server:
  ```
  $ flask run
  ```

5. Navigate to [http://localhost:5000](http://localhost:5000)

You are done with the setup now!

------------------------------------------

### 📝 To-do List

- [ ] Add Email Queuing, Snooze a mail, create drafts.
- [ ] Implement other near features like Gmail.
- [ ] Create App for the same. 

------------------------------------------


### :page_with_curl: Acknowledgements & References

- Flask Documentation - https://flask.palletsprojects.com/en/1.1.x/

-----------------------------------

<h3 align="center"><b>Developed with :heart: by <a href="https://github.com/RugvedB">Rugved</a>, <a href="https://github.com/tushargithub44"> Tushar</a> and <a href="https://github.com/HardikAsher17">Hardik</a> </b></h1>
