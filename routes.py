from flask import jsonify, request, Blueprint , render_template
from database import db_conn
from bson.objectid import ObjectId


api = Blueprint('api', __name__)


@api.route('/' , methods=['GET'])
def root_path():
    return render_template( 'index.html')

@api.route('/api/login', methods=['POST'])
def login_user():
    return "logged in user"

@api.route('/api/users', methods=['GET'])
def get_users():
    try:
        db_connection = db_conn()
        if db_connection is not False:
            db_users = db_connection.users.find()
            users_list = []

            for user in db_users:
                new_user = {'user_id': str(user['_id']),
                            "email": user['email']}
                users_list.append(new_user)
            return jsonify( users_list) , 200
        else:
            return jsonify({'error': 'Database connection failed'}), 500
    except Exception as error:
        print(error)
        return {'error': "server error"} , 500

@api.route('/api/user/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        db_connection = db_conn()
        if db_connection is not False:
            user_id = ObjectId(user_id)
            user = db_connection.users.find_one({'_id': user_id})

            if user:
                return {'user_id': str(user['_id']),
                        "email": user['email']} , 200
            else:
                return {'error': "user not found"} , 400
        else:
            return jsonify({'error': 'Database connection failed'}), 500
    except Exception as error:
        return {'error': "server error"} , 500

@api.route('/api/user', methods=['POST'])
def create_user():
    try:
        db_connection = db_conn()
        if db_connection is not False:
            user_data = request.json
            db_user = db_connection.users.insert_one(user_data)
            
            user_id = str( db_user.inserted_id)
            return {'user_id': user_id,
                    "email": user_data['email']} , 201            
        else:
            return {'error': "database connection failed"}
    except Exception as error:
        print(error)
        return {'error': "server error"} , 500
    
    
@api.route('/api/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    return "update user"


@api.route('/api/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        db_connection = db_conn()
        if db_connection is not False:
            user_id = ObjectId(user_id)
            result = db_connection.users.delete_one({'_id': user_id})
            if result.deleted_count == 1:
                return {'message': f"user_id {user_id} deleted"}
            else:
                return {'error': f'invalid user id {user_id}'}
        else:
            return {'error': "database connection failed"}
    except Exception as error:
        print(error)
        return {'error': "server error"} , 500
    
