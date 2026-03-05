
from ..models import todo
from ..serializers import TodoSerializer
from rest_framework import viewsets
# from rest_framework import status 
# from rest_framework.views import APIView
# from rest_framework.response import Response


class TodoViewSet(viewsets.ModelViewSet):
    queryset = todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer

'''
api로 쏴주는 부분
가상 릴레이션을 만들어서 api로? 쏴줌
'''
# class TodoListAPI(APIView):
#     def get(self, request):

#         todos = todo.objects.all()

#         Serializer = TodoSerializer(todos, many=True)

#         return Response(Serializer.data)

# class TodoCreateAPI(APIView):
#     def post(self, request):
#         serializer = TodoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         todo = serializer.save()
#         return Response(
#             TodoSerializer(todo).data,
#             status=status.HTTP_201_CREATED
#         )

# class TodoRetrieveAPI(APIView):
#     def get(self, request, pk):
#         try:
#             instance = todo.objects.get(pk=pk)
#         except todo.DoesNotExist:
#             return Response(
#                 {"error": "해당하는 해야할 일이 없습니다."},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = TodoSerializer(instance)
#         return Response(serializer.data)

# class TodoUpdateAPI(APIView):
#     def put(self, request, pk):
#         try:
#             instance = todo.objects.get(pk=pk)
#         except todo.DoesNotExist:
#             return Response(
#                 {"error": "해당하는 todo가 없습니다."},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = TodoSerializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         updated_instance = serializer.save()
#         serializer = TodoSerializer(updated_instance)
#         return Response(serializer.data)
    
#     def patch(self, request, pk):
#         try:
#             instance = todo.objects.get(pk=pk)
#         except todo.DoesNotExist:
#             return Response(
#                 {"error": "해당하는 todo가 없습니다."},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = TodoSerializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         updated_instance = serializer.save()
#         serializer = TodoSerializer(updated_instance)
#         return Response(serializer.data)


# class TodoDeleteAPI(APIView):
#     def delete(self, request, pk):
#         try:
#             instance = todo.objects.get(pk=pk)
#         except todo.DoesNotExist:
#             return Response(
#                 {"error": "해당하는 todo가 없습니다."},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
