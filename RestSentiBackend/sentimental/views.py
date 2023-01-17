from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Records
from .serializers import viewSerializer,postSerializer
from .sentimentanalyser import sentiment_predict
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

@api_view(['GET'])
def user_records(request):
    records = Records.objects.all()
    serializer = viewSerializer(records, many=True)
    return Response(serializer.data)

    
@api_view(['POST'])
def add_new(request):
    new_data = JSONParser().parse(request)
    serializer = postSerializer(data=new_data)
    if serializer.is_valid():
        records = Records.objects.filter(uid=str(new_data['uid']),sentance=str(new_data['sentance']))
        if records.count():
            records = records[0]
            serializer2 = viewSerializer(records)
            return Response(serializer2.data)
        sentiment = sentiment_predict(str(new_data['sentance']))
        serializer.save(result=sentiment[1])
        records = Records.objects.filter(uid=str(new_data['uid']),sentance=str(new_data['sentance']))[0]
        serializer2 = viewSerializer(records)
        return Response(serializer2.data)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def records_by_userid(request,pk):
    records = Records.objects.filter(uid=pk)
    serializer = viewSerializer(records, many=True)
    return Response(serializer.data)