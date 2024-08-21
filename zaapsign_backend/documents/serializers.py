from rest_framework import serializers
from .models import Document, Signer

class SignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signer
        fields = ['id', 'name', 'email']

class DocumentSerializer(serializers.ModelSerializer):
    signers = SignerSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = ['id', 'name', 'open_id', 'token', 'status', 'created_by', 'company', 'created_at', 'signers']
