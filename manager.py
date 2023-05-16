from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Leave

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def approve_reject_leave(request):
    if request.user.is_manager:
        leave_id = request.data.get('leave_id')
        status = request.data.get('status')

        try:
            leave = Leave.objects.get(id=leave_id)

            if leave.status == 'pending':
                leave.status = status
                leave.save()
                return Response({'message': 'Leave status updated successfully.'})
            else:
                return Response({'error': 'Leave has already been processed.'}, status=status.HTTP_400_BAD_REQUEST)
        except Leave.DoesNotExist:
            return Response({'error': 'Leave not found.'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'Only managers can perform this action.'}, status=status.HTTP_403_FORBIDDEN)
