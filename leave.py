from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Leave

@api_view(['POST'])
def apply_leave(request):
    if request.user.is_authenticated:
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        if start_date and end_date:
            leave = Leave.objects.create(user=request.user, start_date=start_date, end_date=end_date)
            return Response({'message': 'Leave application submitted successfully.', 'id': leave.id})
        else:
            return Response({'error': 'Missing required data.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'User authentication failed.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def leave_history(request):
    if request.user.is_authenticated:
        leaves = Leave.objects.filter(user=request.user)
        leave_history = []

        for leave in leaves:
            leave_data = {
                'id': leave.id,
                'start_date': leave.start_date,
                'end_date': leave.end_date,
                'status': leave.status,
            }
            leave_history.append(leave_data)

        return Response(leave_history)
    else:
        return Response({'error': 'no leave exist.'}, status=status.HTTP_401_UNAUTHORIZED)
