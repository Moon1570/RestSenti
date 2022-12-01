from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Records
from .serializers import viewSerializer,postSerializer
from .sentimentanalyser import sentiment_predict

@api_view(['GET'])
def user_records(request):
    records = Records.objects.all()
    serializer = viewSerializer(records, many=True)
    return Response(serializer.data)

    
@api_view(['POST'])
def add_new(request):
    serializer = postSerializer(data=request.data)
    if serializer.is_valid():
        sentiment = sentiment_predict(str(request.data['sentance']))
        serializer.save(result=sentiment[1])
        record = Records.objects.filter(uid=request.data['uid'],sentance=request.data['sentance'],result=sentiment[1])
        serializer = viewSerializer(record[0]);
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def records_by_userid(request,pk):
    records = Records.objects.filter(uid=pk)
    serializer = viewSerializer(records, many=True)
    return Response(serializer.data)