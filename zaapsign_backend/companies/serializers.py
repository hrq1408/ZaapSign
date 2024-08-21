from rest_framework import serializers
from .models import Company, Document, Signer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class SignerSerializer(serializers.ModelSerializer):
    document = serializers.PrimaryKeyRelatedField(queryset=Document.objects.all())

    class Meta:
        model = Signer
        fields = ['id', 'name', 'email', 'phone_number', 'status', 'token', 'document']

class DocumentSerializer(serializers.ModelSerializer):
    signers = SignerSerializer(many=True, required=False)

    class Meta:
        model = Document
        fields = ['id', 'name', 'open_id', 'token', 'status', 'created_at', 'signers']

    def create(self, validated_data):
        signers_data = validated_data.pop('signers', [])
        document = Document.objects.create(**validated_data)
        
        signers = [Signer(document=document, **signer_data) for signer_data in signers_data]
        Signer.objects.bulk_create(signers)
        
        return document

