from rest_framework import viewsets
from .models import Company, Document, Signer  # Importe os modelos necessários
from .serializers import CompanySerializer, DocumentSerializer, SignerSerializer  # Importe os serializadores necessários

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class SignerViewSet(viewsets.ModelViewSet):
    queryset = Signer.objects.all()
    serializer_class = SignerSerializer
