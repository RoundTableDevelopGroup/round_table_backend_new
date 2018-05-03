from main.models import Image
from django.shortcuts import HttpResponse
import json
import uuid


MEDIA_SERVER = 'http://127.0.0.1:8000/media/'


class ImageTool:
    @staticmethod
    def get_new_random_file_name(file_name):
        find_type = False
        for c in file_name:
            if c == '.':
                find_type = True
        if find_type:
            type = file_name.split('.')[-1]
            return str(uuid.uuid1()) + '.' + type
        else:
            return str(uuid.uuid1())


def image_upload(request):
    source = request.FILES.get('image')
    if source:
        source.name = ImageTool.get_new_random_file_name(source.name)
        image = Image(
            img=source
        )
        image.save()
        return HttpResponse(json.dumps({
            'success': True,
            'path': MEDIA_SERVER + image.img.url
        }))
    else:
        return HttpResponse(json.dumps({
            'success': False,
            'error_code': 100
        }))

