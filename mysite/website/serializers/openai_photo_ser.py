from rest_framework import serializers
from website.models import OpenAI_Photo

class OpenAIPhotoSerializers(serializers.ModelSerializer):
    fileName = serializers.ReadOnlyField(source='file_name')
    filePath = serializers.FileField(source='file_path',max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = OpenAI_Photo
        fields = ('fileName','filePath', 'describe')