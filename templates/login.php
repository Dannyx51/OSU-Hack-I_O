<!DOCTYPE html>
<html>
    <style>
        .button{
            border: none;
            color: darkcyan;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
        

        
    </style>

    <head>
        <meta charset = "utf-8"/>
        <title>Please login to your account. :)</title>
    </head>
    <body>
        <form action = "verify.php" method = "get"> 
            <label for = "username">Enter username:</label>
            <input type = "text" id = "username" name = "username"><br><br>
            <label for = "password">Enter password:</label>
            <input type = "text" id = "password" name = "password"><br><br>
            <input type = "button" id = "loginButton" name = "loginButton" value = "Log in"></input>
            
        </form>
    </body>

</html>