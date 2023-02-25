from django.shortcuts import render
# from django.views import View
from .serializers import PostSerializers
from rest_framework.permissions import IsAuthenticated
from .models import Post
from rest_framework import generics

# class Get_all(View):
#     def get(self, request):
#         posts = Post.objects.all()
#         return render(request, 'blog/index.html', context={'posts': posts})

class PostsList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers
    queryset = Post.objects.all()

class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializers

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
