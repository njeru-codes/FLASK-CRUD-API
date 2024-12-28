from flask import Flask
from routes import api
import os
from database import db_conn

app = Flask(__name__)




# register routes
app.register_blueprint(api)







if __name__ =="__main__":
    try:
        production = os.environ.get('PRODUCTION')
        if production == "LIVE":
            app.run( debug=False)
        
        app.run( debug=True)
    except Exception as error:
        print( str(error))
    finally:
        # release or clear rescources
        pass