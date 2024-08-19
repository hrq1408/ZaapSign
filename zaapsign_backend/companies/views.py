import json
import requests
from django.conf import settings
from rest_framework.exceptions import APIException
from rest_framework.views import APIView

class CreateDocumentView(APIView):

    def get_jwt_token(self):
        """Obtém o token JWT, armazenando-o em uma variável de ambiente ou cache."""
        jwt_token = getattr(settings, "ZAPSIGN_JWT_TOKEN", None)
        if jwt_token:
            print("JWT token já existente:", jwt_token)
            return jwt_token

        
        auth_url = "https://api.zapsign.com.br/api/v1/auth/token/"
        auth_data = {
            "username": settings.ZAPSIGN_USERNAME,
            "password": settings.ZAPSIGN_PASSWORD
        }
        auth_response = requests.post(auth_url, json=auth_data)
        print("Resposta da autenticação:", auth_response.status_code, auth_response.text)

        if auth_response.status_code != 200:
            raise APIException(f"Failed to authenticate with ZapSign. Status code: {auth_response.status_code}, Response: {auth_response.text}")

        auth_response_data = auth_response.json()
        jwt_token = auth_response_data.get("access")
        print("Novo JWT token:", jwt_token)

        
        settings.ZAPSIGN_JWT_TOKEN = jwt_token

        return jwt_token

    def perform_create(self, serializer):
        document = serializer.save()

        
        jwt_token = self.get_jwt_token()

        
        zap_sign_api_url = "https://sandbox.api.zapsign.com.br/api/v1/docs/"
        document_data = {
            "api_token": settings.ZAPSIGN_API_TOKEN,
            "name": document.name,
            "lang": "pt-br",
            "file_url": document.file_url
        }

        try:
            response = requests.post(
                zap_sign_api_url,
                headers={
                    'Authorization': f'Bearer {jwt_token}',
                    'Content-Type': 'application/json'
                },
                data=json.dumps(document_data)
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            raise APIException(f"HTTP error occurred: {http_err}, Response: {response.text}")
        except Exception as err:
            raise APIException(f"Other error occurred: {err}")

        if response.status_code == 201:
            document.zapsign_id = response.json().get("id")
            document.save()
        else:
            raise APIException(f"Failed to create document in ZapSign. Status code: {response.status_code}, Response: {response.text}")

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
