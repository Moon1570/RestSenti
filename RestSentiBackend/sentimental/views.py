from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Records
from .serializers import RecordsSerializer



@api_view(['POST'])
def sa(request):

    prerec=Records.objects.get(sentance=request.data["sentance"],uid=request.data["uid"])
    if prerec.exists():
        return Response(prerec.data)
    else:
        result = getSentiment(request.data["sentance"])
        request.data["result"]=result
        record = RecordsSerializer(data=request.data)
        if record.is_valid():
            record.save()
            return Response(record.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def records(request):
    rec=Records.objects.get(uid=request.data["uid"])
    return Response((rec.data))
