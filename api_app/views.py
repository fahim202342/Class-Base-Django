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
        serializer_data = StudentSerializer(data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({
                'success': True,
                'messages': 'Student Data Create Successfully',
                'data': serializer_data.data
            })
        return Response({
            'success': False,
            'error': serializer_data.errors
        })
        


class StudentDetailListAPI(APIView):
    def get_data(self, t_id):
        try:
            student_data = StudentModel.objects.get(id = t_id)
            return student_data
        except:
            return Response({
                'success': False,
                'messages':'Student Data Not Found'
            })
    def get(self, request, t_id):
        
        student_data = self.get_data(t_id)
        serializer_data = StudentSerializer(student_data)
        return Response({
            'success': True,
            'messages': 'Student Data Get Successfully',
            'data': serializer_data.data
        })
    
    def put(self, request, t_id):
        student_data = self.get_data(id=t_id)
        serializer_data =StudentSerializer(student_data, data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({
            'success': True,
            'messages': 'Student Data Updated Successfully',
            'data': serializer_data.data
        })

    def patch(self, request, t_id):
        student_data = self.get_data(id = t_id)
        serializer_data = StudentSerializer(student_data, data = request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({
                'success': True,
                'messages': 'Student Data Updated Successfully',
                'data': serializer_data.data
            })
        return Response({
            'success': False,
            'error': serializer_data.errors
        })
        
    def patch(self, request, t_id):
        self.get_data(id = t_id).delete()
        return Response({
            'success': True,
            'messages':'Student Data Deleted Successfully',
            'data': []
        })

        

        
