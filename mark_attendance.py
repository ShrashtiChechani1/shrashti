
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Attendance
from datetime import datetime

@api_view(['POST'])
def mark_attendance(request):
    user_id = request.data.get('user_id')
    check_in = request.data.get('check_in')
    check_out = request.data.get('check_out')
    check_in =datetime.strptime(check_in, "%d-%m-%Y")
    if user_id and check_in:
        attendance = Attendance(user_id=user_id, check_in=check_in, check_out=check_out)
        attendance.save()
        return Response({'message': 'Attendance marked successfully.', 'id': attendance.id})
    else:
        return Response({'error': 'Missing required data.'}, status=400)
