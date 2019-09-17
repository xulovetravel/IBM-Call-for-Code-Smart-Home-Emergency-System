# IBM-Call-for-Code-Smart-Home-Emergency-System
This is the repo for IBM Call For Code Internal team Smart Home Emergency System. In emergencies (e.g. earthquake), currently there are no efficient ways for rescuers to communicate, locate, and evaluate survivors’ situations quickly, conveniently, and accurately, to accomplish well-planned and successful rescue works. To solve this problem, we propose and develop Smart Home Emergency System (SHES), which facilitates the rescue works during emergencies.
# Smart Home Emergency System (SHES) Implementation
•	User Interface with Mobile Phone or Google Home
In our implementation and demo, we used Android phone and Google Home to demonstrate the user interaction through voice commands (it also works with texts). Upon waking up Google Assistant, the user can say "Talk to Smart Home Emergency System" to enable our customized emergency conversation, which is designed with Google DialogFlow and Firebase. After the response of SHES, if user says "I need help", it will ask for more details. With further detailed reply of "I cannot move", SHES will update this content into Firebase database, and let the user know "help is on the way".
 

•	IBM FYRE Private Cloud Data Process Server
Once the previously mentioned Firebase database content updated, our IBM Cloud Data Process Server (implemented with Python) will detect the change, and update this info into our SHES database, along with other information, such as latitude, longitude, address, postal code, and voice message.
 
•	IBM Cognos Analytics (CA) Modelling and Dashboard Display
IBM Cognos Analytics will monitor the SHES database, and display survivors' locations on map based on the location information from database, with all other related information. In this way, rescuers are able to accurately locate the survivors and understand their current situations, then plan and conduct corresponding rescue works! The CA Dashboard url is here, and can be logged in with namespace LDAP, username hmiller, and password hillock, then search for smart home emergency dashboard.

