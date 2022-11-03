from .models import Post
from commets.serializers import CommentSerializer
from interactions.serializers import InteractionSerializer


def get_comments_list(obj: Post):
    comments = obj.comments
    import ipdb
    ipdb.set_trace()
    print()
    # return CommentSerializer(comments, many=True)
    return 'seila'


def get_interactions_report(obj: Post):
    interactions = obj.interactions
    return InteractionSerializer(interactions, many=True)
