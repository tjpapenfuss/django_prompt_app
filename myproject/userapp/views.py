# userapp/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
import uuid
import json

# Connect to MongoDB
import uuid
from userapp import users_db

# Create (or use existing) collection for users
user_collection = users_db['users']

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_name = data['user_name']
        name = data['name']
        email = data['email']
        
        existing_user = user_collection.find_one({"user_name": user_name})
        if existing_user:
            return JsonResponse({"error": f"User with ID {user_name} already exists."}, status=400)
        
        user = {
            "user_id": str(uuid.uuid4()), 
            "user_name": user_name,
            "name": name,
            "email": email
        }
        
        user_collection.insert_one(user)
        return JsonResponse({"message": f"User {name} created successfully."})

    return JsonResponse({"error": "Invalid request method."}, status=405)

def get_user_info(request, user_name):
    user = user_collection.find_one({"user_name": user_name})
    if user:
        return JsonResponse(user)
    return JsonResponse({"error": f"User {user_name} doesn't exist."}, status=404)

def get_user_id(request, user_name):
    user = user_collection.find_one({"user_name": user_name})
    if user:
        return JsonResponse({"user_id": user['user_id']})
    return JsonResponse({"error": f"Username {user_name} doesn't exist."}, status=404)

def get_user_name(request, user_id):
    user = user_collection.find_one({"user_id": user_id})
    if user:
        return JsonResponse({"user_name": user['user_name']})
    return JsonResponse({"error": f"User ID {user_id} doesn't exist."}, status=404)
