from website import create_app


app = create_app() #calling create app function and assign the returned value to variable app
if __name__ == '__main__':  # checks if the script is being run directly as the main entry point of the program
    app.run(debug=True)      # the .run method starts a development server and listens for incoming requests. Setting debug = True, enables debig mode, which provides detailed error msg and automatic reloading of the application when changes are made.
      # debug = True helps us from manually re-running the server. 