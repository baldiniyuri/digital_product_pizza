from rest_framework.authtoken.models import Token
from authentication.models import User    
from django.db.models import Q


class CoreUtils:

    def check_user_token(self, request, user_id: int):
        user_id_token = Token.objects.get(user=user_id)
        request_token = request.auth.key
            
        if user_id_token.key == request_token:
            return True
            
        return False


    def delete_user_token(self, user_id: int):
        token_to_delete = Token.objects.get(user=user_id)
    
        if token_to_delete:
            token_to_delete.delete()
            return True

        return False


    def find_user(self, user_id: int):
        found = User.objects.filter(id=user_id)
        if found:
            return True
        return False


    def check_sql_injection(self, request):
        characters_list = ["'", "#", "--", "-", "OR", "AND"]

        for char in characters_list:
            if char in request.data["email"]:
                return True
            
            return False
        
    def check_user_exists(self, request):
        if User.objects.filter(Q(email=request.data['email']) | Q(cpf=request.data["cpf"])).exists():
            return True
        return False