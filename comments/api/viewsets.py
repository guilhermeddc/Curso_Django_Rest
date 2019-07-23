from rest_framework.viewsets import ModelViewSet
from comments.models import Comments
from .serializers import CommentsSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
