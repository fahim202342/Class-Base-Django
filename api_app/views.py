from rest_framework.views import APIView
from rest_framework.response import Response
from api_app.serializers import *
from api_app.models import *


class StudentCreateListAPI(APIView):
    def get(self, request):
        student_data = StudentModel.objects.all()
        serializer_data = StudentSerializer(student_data, many=True)
        return Response({
            'success': True,
            'messages': 'Student Data Get Successfully',
            'data': serializer_data.data
        })

    def post(self, request):
        serializer_data = StudentSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({
                'success': True,
                'messages': 'Student Data Created Successfully',
                'data': serializer_data.data
            })
        return Response({
            'success': False,
            'error': serializer_data.errors
        })


class StudentDetailListAPI(APIView):

    def get_object(self, t_id):
        try:
            return StudentModel.objects.get(id=t_id)
        except StudentModel.DoesNotExist:
            return None

    def get(self, request, t_id):
        student_data = self.get_object(t_id)
        if not student_data:
            return Response({
                'success': False,
                'messages': 'Student Data Not Found'
            })

        serializer_data = StudentSerializer(student_data)
        return Response({
            'success': True,
            'messages': 'Student Data Get Successfully',
            'data': serializer_data.data
        })

    def put(self, request, t_id):
        student_data = self.get_object(t_id)
        if not student_data:
            return Response({'success': False, 'message': 'Not Found'})

        serializer_data = StudentSerializer(student_data, data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({
                'success': True,
                'messages': 'Student Updated Successfully',
                'data': serializer_data.data
            })

        return Response({
            'success': False,
            'error': serializer_data.errors
        })

    def patch(self, request, t_id):
        student_data = self.get_object(t_id)
        if not student_data:
            return Response({'success': False, 'message': 'Not Found'})

        serializer_data = StudentSerializer(student_data, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({
                'success': True,
                'messages': 'Student Partially Updated',
                'data': serializer_data.data
            })

        return Response({
            'success': False,
            'error': serializer_data.errors
        })

    def delete(self, request, t_id):
        student_data = self.get_object(t_id)
        if not student_data:
            return Response({'success': False, 'message': 'Not Found'})

        student_data.delete()
        return Response({
            'success': True,
            'messages': 'Student Deleted Successfully',
            'data': []
        })