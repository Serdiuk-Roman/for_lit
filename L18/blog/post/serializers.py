from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.generics import GenericAPIView

from post.models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'is_active', 'user')

    # name = serializers.CharField(max_length=20)
    # description = serializers.CharField(max_length=255)
    # is_active = serializers.BooleanField()
    # user = serializers.IntegerField(source='user_id', read_only=True)


class PostSerializer(serializers.ModelSerializer):
    # category_repr = CategorySerializer(
    #     queryset=Category.objects.all(),
    #     read_only=True,
    #     source='Category.name')
    # category = serializers.HyperlinkedRelatedField(
    #     queryset=Category.objects.all(),
    #     write_only=True
    # )

    class Meta:
        model = Post
        fields = ('id', 'category',
                  'user', 'title', 'context', 'status')
        # read_only_fields = ('account_name',)
        # extra_kwargs = {'password': {'write_only': True}}

    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    # category = CategorySerializer()
    # user = serializers.IntegerField(source='user_id')
    # title = serializers.CharField(max_length=255)
    # context = serializers.CharField()
    # create = serializers.DateTimeField(read_only=True)
    # update = serializers.DateTimeField(read_only=True)
    # status = serializers.ChoiceField(choices=Post.STATUSES, default=0)

    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.user = validated_data.get('user', instance.user)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.context = validated_data.get('context', instance.context)
    #     instance.create = validated_data.get('create', instance.create)
    #     instance.update = validated_data.get('update', instance.update)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.save()
    #     return instance


# from post.models import Post, Category
# from post.serializers import PostSerializer, CategorySerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# p = Post.objects.first()
# ser = PostSerializer(p, many=True)
# ser.data
