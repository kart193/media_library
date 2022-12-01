# media_library
Media Library

Abstract
Media Library is the web application which can be used to add, list, edit and delete media files of the user. It can be accessed using web browsers. It can be enhanced to facilitate multiple users. The data is persisted and retrieved from postgres database. The purpose of this document is to explain the approaches that were taken to build this application, design pattern and the areas which could be improved. This work shows an exploratory approach towards the requirements and built a fully functional media library. Ease of use, performance and data persistence are few of the things that are considered throughout the entire development process.
 ![image](https://user-images.githubusercontent.com/119109184/205102514-ecb406aa-ae33-4250-b064-549ed25fdf92.png)


1	Introduction
The web application is developed using the Python’s Flask API and HTML. Postgres object-relational database is used as a data store in this application. Hypertext Markup Language (HTML) is used for designing the web page and to display it in a web browser. The following sections show the application architecture and the functionalities.

2	Architecture
Web application architecture is the mechanism that deter- mines how the different application components communi- cate with each other. In other words, the way the client and the server are connected and established by web application architecture.
 
 
In this application Postgres database is used as the data store. There are other options like MySQL.  The reason for selecting Postgres database are as follows

<img width="167" alt="image" src="https://user-images.githubusercontent.com/119109184/205102854-5269bef8-c3a6-4d6a-8ae3-e94d409142f7.png">

•	It is open-source relational database.
•	Simple to use with python using available features. 
•	It offers more sophisticated data types.
•	Performs well with complex queries
•	It supports modern application features.
•	Faster when dealing with large datasets and read-write operations
•	It has PGAdmin web-based GUI management application used to communicate with Postgres on both local and remote server.


2.1 Database design
The database design was finalized based on the parameters in such a way that the collected data is persisted, well organized and can be easily retrieved, updated and deleted. The following steps were followed to derive at this database solution.

1.	Determining the purpose of the database.
2.	Gather and organize the information required.
3.	Convert the information into table columns 
4.	Specify primary keys and auto-increment if required 
5.	Set right data type for the columns

For the given requirement, single entity should be sufficient in terms of a single user use case. Considering the type of media files to be accessed say audio, video and game files, storing them straight on the database would not be a viable solution. Instead, just storing the references to the media files in the database will be more efficient. 
The usual approach is to store your media files in a specific directory and reference the URL of the media file in your database.   And the same is applicable in our application. 
 
 
2.2 Framework Used
Flask is the microframework used for developing this web applications using python. It is implemented on Werkzeug and Jinja2. Advantages of using Flask framework are: 
•	Easy to integrate Web APIs with Front-end using flask route and requests options. 
•	Reduces the overall development time
•	Flask is the good solution for simple web application with fewer pages. 
•	Flask is considered more pythonic than Django
•	We have SQLAlalchemy SQL toolkit and object relation mapper.

Internal workflow details: 

<img width="487" alt="image" src="https://user-images.githubusercontent.com/119109184/205102752-f2c9bac4-27bf-424e-85b0-1c3ac0ac481d.png">

1.	When the user adds the files – the file location or the meta data gets saved to the postgres database along with the actual copy of the file stored to a directory in the predefined path. 
2.	Retrieving media file to show in the UI – Directly query from the database and provide the file details like name and type. Actual file from the directory is not accessed in this case as the requirement does include playbacks or viewing of the files. 
3.	Type of the file is obtained through the python method before storing to the database. 
4.	To list each file format data separately – we filter data based on the format stored in the database. 
5.	Both update and deletion are made on both the database metadata and the folder directory.

2.3 Web Page Design
We have used HTML to design and structure the contents of the web page. We have used Cascading style sheets over the HTML tags to improve their appearance. The mapping annotations inside the controllers let us map HTTP requests from the HTML to specific controller methods.

 <img width="216" alt="image" src="https://user-images.githubusercontent.com/119109184/205103785-b23b6a92-381b-420e-be86-73c4bb5ec27d.png">

Some of the reasons and the advantages for preferring HTML are:
•	HTML is supported by all the Web Browsers.
•	HTML is Easy to write and edit.
•	HTML can integrate easily with other languages.
•	HTML is lightweight.

3	Application User Interface

<img width="293" alt="image" src="https://user-images.githubusercontent.com/119109184/205103855-9262814b-5e3e-4af5-8cb9-6d27822cd898.png">

Media Library is a single HTML page application.  The page is to add, edit, delete and edit media libraries.
The following is the landing page of the application before adding any media files.

 
Figure Landing Page of the Application

Media list view 

<img width="308" alt="image" src="https://user-images.githubusercontent.com/119109184/205103885-52d87ebd-52df-46da-a1df-a55bb3531975.png">


Once user add the media file into the application, the media files will be listed on the application with the file name and type of the file being added. Following is the corresponding view – 

 
4	Performance
Web application performance is important for user accessibility and for other important website metrics that serve the goals of an organization or business. Good or bad website performance is directly proportional to user experience, as well as the overall effectiveness of most sites. the following performance considerations were given a thought during the development of the app.
Files are stored in directory and only the reference of file is stored in database to reduce performance issue.
Primitive data types are used wherever possible. 
Only the required dependencies were used to make         the runnable file lightweight.
5	Testing
<img width="113" alt="image" src="https://user-images.githubusercontent.com/119109184/205103991-e427d55f-74ea-4951-ba2a-409761bc9470.png">

Data Integrity testing is done as part of the Testing phase. I have used PyTest for the same. PyTest is a testing framework that allows users to write test codes using Python programming language. It helps you to write simple and scalable test cases for databases, APIs, or UI. I have used PyTest fixtures, function scope fixtures and parameterization. 

Following is the step to execute the test cases added. 
<img width="517" alt="image" src="https://user-images.githubusercontent.com/119109184/205103970-3c0448a1-2ed0-4504-b549-61d79f4182f6.png">

6	Happy Flow of the application
The Happy flow and a manual for the entire web application is given below step by step. Please follow these instructions to navigate through the web application.
7.1	Step 1
The landing page of the application can be reached through the URL: http://localhost:5004/dashboard/all 

<img width="249" alt="image" src="https://user-images.githubusercontent.com/119109184/205104081-774822fa-f078-4030-a8df-98b95a4c5115.png"> 
<img width="234" alt="image" src="https://user-images.githubusercontent.com/119109184/205104105-1898d547-e408-4b18-b842-104fabdac855.png">

1.	First part of the web page is the provision to select file/files using choose files option to choose files from your local system and upload the same into the library using Upload button. 
2.	App allows you to upload files of specific formats. (Video, Music, Games) This can be achieved through multiple ways.  I have tried two in this workflow - Through python method to find the format and save into database based on the same and HTML accept attribute to accept only specific file formats.  
3.	Second part is you have option to list only one type of file – say Video button to list video files, audio for audio files and all to list all files. 
4.	Delete operation – I have incorporated both single row deletes, and multiple row deletes in the application.
a.	For single row delete – there is a delete button available in each row.
b.	For multi row delete – checkbox is added to select rows to be deleted. 
5.	Edit option is available in each row to edit the title of the file.  

7	Improvisation Ideas 

•	More table operations like sorting, filtering could be added.
•	Application can have login page for more privacy and security factors.
•	Restricting the user to edit the file extension
•	Error popups on various conditions like when the user tries to save with the same name or same file.  If upload is clicked without any file chosen and so on. Now the application will restrict such flows but it won’t notify the user. 
•	Adding scroll button for accessing a larger list.
•	Including lazy loading in case of large datasets. 
•	

8	Deploying steps 

Unzip the  mediaLib in your local  and  run  it using    

flask run -p 5004 

5004 is the port where my application is running in my local. 
I have setup postgres database in my local to connect it with the application. 
Steps to setup the same https://www.prisma.io/dataguide/postgresql/setting-up-a-local-postgresql-database ![image](https://user-images.githubusercontent.com/119109184/205102169-0b5fa870-7f49-4517-988e-99f13e32c6e6.png)

