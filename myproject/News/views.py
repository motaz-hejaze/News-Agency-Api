from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (

	HTTP_400_BAD_REQUEST,
	HTTP_404_NOT_FOUND,
	HTTP_200_OK

	)
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))

def login(request):
	print(request.body)
	# request.boddy is byte object not string object
	username = request.data.get("username")
	password = request.data.get("password")
	print(request.data)
	if username is None or password is None:
		return Response({'error' : 'Please Provide Both Username and Password'},
			status=HTTP_400_BAD_REQUEST)

	user = authenticate(username=username,password=password)
	if not user:
		return Response({'error' : 'Invalid Credentials'},
			status=HTTP_404_NOT_FOUND)

	token , _ = Token.objects.get_or_create(user=user)

	return Response({'token': token.key},
			status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])

def sample_api(request):
	data = {'sample_data':123}
	return Response(data , status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])

def all_news(request):
	all_news = News.objects.all()
	serializer = NewsSerializer(all_news,many=True)
	return Response({
		"News":serializer.data},
		status=HTTP_200_OK
		)

@csrf_exempt
@api_view(["POST"])

def post_a_news(request):
	title = request.data.get("title") 
	body = request.data.get("body")
	reporter_id = request.data.get("reporter_id")
	reporter_country_id = request.data.get("reporter_country_id")
	if title is None or body is None or reporter_id is None or reporter_country_id is None:
		return Response({'error':'Please provide all data'})
	else:
		sent_news = News(
				title=title,
				body=body,
				reporter_id=reporter_id,
				reporter_country_id=reporter_country_id
			)
		sent_news.save()
		serializer = NewsSerializer(sent_news,many=False)
		return Response({
			"Submitted News" : serializer.data},
			status=HTTP_200_OK
			)


@csrf_exempt
@api_view(["PUT"])

def update_a_news(request,id):
	news = News.objects.get(pk=id)
	if news is None:
		return Response({'error':'No data Found'} , status=HTTP_404_NOT_FOUND)
	else:

		title = request.data.get("title") 
		body = request.data.get("body")
		reporter_id = request.data.get("reporter_id")
		reporter_country_id = request.data.get("reporter_country_id")

		if title is None or body is None or reporter_id is None or reporter_country_id is None:
			return Response({'error':'Please provide all data'})
		else:
			news.title = title
			news.body = body
			news.reporter_id = reporter_id
			news.reporter_country_id = reporter_country_id
			news.save()
			serializer = NewsSerializer(news , many=False)
			return Response({
				"Updated News" : serializer.data},
				status=HTTP_200_OK
				)











@csrf_exempt
@api_view(["DELETE"])

def delete_a_news(request,id):
	news = News.objects.get(pk=id)
	if news is None:
		return Response({'error':'No data Found'}, status=HTTP_404_NOT_FOUND)
	else:
		news.delete()
		return Response({'success':'news deleted successfuly'})


