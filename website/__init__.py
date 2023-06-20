from flask import Flask
## __init__ is used to create website folder as a package

# create app function is expected to create and configure the Flask application object.
def create_app():
    app = Flask(__name__)
    app.config['SECRETE_KEY'] = 'dandbaithakdesigheerepeat'
    
    from .views import views
    from .auth import auth
    
    # integrating the blueprint into Flask application, By registering a blueprint, you are telling the Flask application to include and handle the routes,views,templates & static file defined within that blueprint.
    app.register_blueprint(views,url_prefix='/')          
    app.register_blueprint(auth,url_prefix='/')
    
    return app