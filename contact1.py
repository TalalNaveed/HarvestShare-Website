#!/usr/bin/python3


print("Content-Type: text/html\n\n")

import cgi

data = cgi.FieldStorage()

print(""" 
<!DOCTYPE HTML>
<html>

<head>
    <title>Confirmation</title>
    <link type='preconnect' href='https://fonts.googleapis.com'>
    <link type='preconnect" href='https://fonts.gstatic.com" crossorigin>
    <link href='https://fonts.googleapis.com/css2?family=Inter:wght@100;300;400;700;900&display=swap' rel='stylesheet'>
    <link href='css/bootstrap.min.css' type='stylesheet'>
    <link href='css/bootstrap-icons.css" type="stylesheet'>
    <link type='stylesheet' href='css/slick.css'/>
    <link href='css/tooplate-little-fashion.css' type='stylesheet'>
</head>

<body>
    <h1>Thank you for contacting Us! </h1>
    <h3> Here is the information you submitted:</h3> 
    <div class='container'>
""")

for key in data.keys(): 
    print("<li>", key, ":", data[key].value) 

print("""
    </div>
</body>
</html>
""")
