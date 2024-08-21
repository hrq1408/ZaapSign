from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Document, Signer
from .serializers import DocumentSerializer, SignerSerializer
from companies.models import Company
import requests

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        company = Company.objects.get(pk=data['company_id'])

        api_url = "https://sandbox.api.zapsign.com.br/api/v1/docs/"
        headers = {
            "Authorization": f"Token {company.api_token}"
        }
        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code == 201:
            document_data = response.json()
            document = Document.objects.create(
                name=data["name"],
                open_id=document_data["open_id"],
                token=document_data["token"],
                status=document_data["status"],
                created_by=request.user,
                company=company
            )
            for signer_data in data["signers"]:
                Signer.objects.create(
                    name=signer_data["name"],
                    email=signer_data.get("email", ""),
                    document=document
                )
            serializer = self.get_serializer(document)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(response.json(), status=response.status_code)
