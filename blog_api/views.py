from rest_framework import generics
from blog.models import Post
#Import the PostSerializer
from blog_api.serializers import PostSerializer

 
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class =  PostSerializer
     
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer