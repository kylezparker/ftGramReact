import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import ShareForm
from .models import Share
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from .serializers import ShareSerializer

ALLOWED_HOSTS = settings.ALLOWED_HOSTS



def home_view(request, *args, **kwargs):
    print(request.user or None)
    return render(request,"pages/home.html", context={}, status=200 ) 

@api_view(['POST']) # http method the client == POST 
def share_create_view(request, *args, **kwargs):
    serializer = ShareSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


def share_create_view_pure_django(request, *args, **kwargs):
    '''
    REST API Create View -> DRF
    '''
    user = request.user
    if not request.user.is_authenticated:
        user = None
        if (request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'):
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    # print(abc)
    def is_ajax(request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def ajax_test(request):
        if is_ajax(request=request):
            message="this is ajax"
        else:
            message="not ajax"
        return HttpResponse(message)

    # print("ajax", request.is_ajax())
    form = ShareForm(request.POST or None)
    next_url = request.POST.get("next") or None 
    # print("next url", next_url)
    if form.is_valid():
        obj= form.save(commit=False)
        # do other form related logic
        obj.user = request.user
        obj.save()
        if (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
            return JsonResponse(obj.serialize(), status=201) # 201 = created items

        if next_url != None and url_has_allowed_host_and_scheme(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form= ShareForm()
    if form.errors:
        if (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
            return JsonResponse(form.errors, status=400)
    return render(request, 'components/form.html', context={"form": form})

def share_list_view_pure_django(request, *args, **kwargs):
    # REST API VIEW. consume by javascript or swift/java/ios/android
    # return json data
    qs = Share.objects.all()
    shares_list = [x.serialize() for x in qs]
    data = {
        "isUser": False,
        "response":shares_list
    }
    return JsonResponse(data)




@api_view(['GET'])
def share_detail_view(request, share_id, *args, **kwargs):
    qs = Share.objects.filter(id=share_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = ShareSerializer(obj)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def share_list_view(request, *args, **kwargs):
    qs = Share.objects.all()
    serializer = ShareSerializer(qs, many=True)
    return Response(serializer.data)

def share_detail_view_pure_django(request, share_id, *args, **kwargs):
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