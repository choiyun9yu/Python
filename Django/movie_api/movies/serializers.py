from rest_framework import serializers
from .models import Movie, Actor, Review

# class MovieSerializer(serializers.ModelSerializer):
#     # reviews의 타입을 StringRelatedField로 설정
#     reviews = serializers.StringRelatedField(many=True)
#     class Meta:
#         model = Movie
#         fields = ['id', 'name', 'reviews', 'opening_date', 'running_time', 'overview']
#         read_only_fields = ['reviews']


# class ReviewSerializer(serializers.ModelSerializer):
#     movie = serializers.StringRelatedField()
#     class Meta:
#         model = Review
#         fields = ['id', 'movie', 'username', 'star', 'comment', 'created']

# class MovieSerializer(serializers.ModelSerializer):
#     # !주의 MovieSerializer 선언 전에 ReviewSerializer가 선언되어야함.
#     reviews = ReviewSerializer(many=True, read_only=True)
#     class Meta:
#         model = Movie
#         fields = ['id', 'name', 'reviews', 'opening_date', 'running_time', 'overview']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'reviews', 'opening_date', 'running_time', 'overview']
        read_only_fields = ['reviews']

class ReviewSerializer(serializers.ModelSerializer):
    # !주의 ReviewSerializer 선언 전에 MovieSerializer가 선언되어야함.
    movie = MovieSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'movie', 'username', 'star', 'comment', 'created']

class ActorSerializer(serializers.ModelSerializer):
    class Meta :
        model = Actor
        fields = '__all__'
        
# class MovieSerializer(serializers.Serializer):
#     # 사용할 필드 이름은 꼭 모델에서 사용하는 필드 이름과 일치시켜야 한다.
#     id = serializers.IntegerField(read_only=True)   # read_only : 필드를 조회할 때만 사용하고 싶은 경우 사용
#     name = serializers.CharField()
#     opening_date = serializers.DateField()
#     running_time = serializers.IntegerField()
#     overview = serializers.CharField()

#     def create(self, validated_data):   # 파라미터로 받은 validated_data는 유효성 검사를 마친 데이터라는 의미
#         return Movie.objects.create(**validated_data)   # **는 언팩킹

#     def update(self, instance, validated_data): # instance는 수정할 모델 객체 의미
#             # get(keyName, default) : 키값있으면 그거 가져오고 없으면 기본값 반환
#             instance.name = validated_data.get('name', instance.name)
#             instance.opening_date = validated_data.get('opening_date', instance.opening_date)
#             instance.running_time = validated_data.get('running_time', instance.running_time)
#             instance.overview = validated_data.get('overview', instance.overview)
#             instance.save()
#             return instance 

# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ['id', 'movie', 'username', 'star', 'comment', 'created']
#         extra_kwargs = {
#             'movie': {'read_only': True},
#         }


# class ActorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     gender = serializers.CharField()
#     birth_date = serializers.DateField()

#     def create(self, validated_data):
#         return Actor.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#          instance.name = validated_data.get('name', instance.name)
#          instance.gender = validated_data.get('gender', instance.gender)
#          instance.birth_date = validated_data.get('birth_date', instance.birth_date)
#          instance.save()
#          return instance

