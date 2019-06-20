from rest_framework import serializers

from .models import News

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = ('id','title','body','reporter_id','reporter_country_id','created_at','updated_at')
		read_only_fields = ('id','created_at','updated_at')