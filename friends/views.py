from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Share
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request,"pages/home.html", context={}, status=200 ) 

def share_list_view(request, *args, **kwargs):
    # REST API VIEW. consume by javascript or swift/java/ios/android
    # return json data
    qs= Share.objects.all()
    shares_list= [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "isUser": False,
        "response":shares_list
    }
    return JsonResponse(data)

def share_detail_view(request, share_id, *args, **kwargs):
    # REST API VIEW. consume by javascript or swift/java/ios/android
    # return json data
    data = {
        "id": share_id,
        #  "image_path":obj.image.url
    }
    status= 200
    try:
        obj= Share.objects.get(id=share_id)
        data['content'] = obj.content
    except:
        data['message']= "Not found"
        status= 404

    return JsonResponse(data, status=status)