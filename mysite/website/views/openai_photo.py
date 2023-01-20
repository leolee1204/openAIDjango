from rest_framework.response import Response
from website.models import OpenAI_Photo
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from rest_framework import permissions, views
import openai
import requests
from website.serializers import OpenAIPhotoSerializers
import io

class OpenAIPhotoCreateAPIView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = []

    def post(self, request):
        describe = request.data.get('describe')
        numbers = request.data.get('numbers')
        file_name = request.data.get('fileName')

        openai.organization = "insert your organization"
        openai.api_key = "insert your API-KEY"

        response = openai.Image.create(
            prompt=describe,
            n=int(numbers),
            size="1024x1024"
        )
        for i,data in enumerate(response['data']):
            res_image = requests.get(data['url'])
            if res_image.status_code == 200:
                byte_stream = io.BytesIO(res_image.content)  # 把請求到的資料轉換為Bytes位元組流
                input_image = Image.open(byte_stream) # Image開啟二進位制流Byte位元組流資料

                w, h = input_image.size
                input_image.thumbnail((w,h), Image.ANTIALIAS)

                pic_io = BytesIO() # 建立一個空的Bytes物件
                input_image.save(pic_io, input_image.format)

                pic_file = InMemoryUploadedFile(
                    file=pic_io,
                    field_name=None,
                    name=f'{file_name}-{str(i)}.png',
                    content_type='image/png',
                    size=input_image.size,
                    charset=None
                )

                defaults = dict()
                defaults['describe'] = describe
                defaults['file_path'] = pic_file
                defaults['file_name'] = f'{file_name}.png'

                OpenAI_Photo.objects.update_or_create(
                    pk=request.data.get('id'),
                    defaults=defaults,
                )
        return Response({"massage":True})

class OpenAIPhotoListAPIView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = []

    def get(self, request):
        openai_photos = OpenAI_Photo.objects.all()
        serializer_users = OpenAIPhotoSerializers(
            openai_photos, many=True, context={"request": request}
        )
        return Response(serializer_users.data)