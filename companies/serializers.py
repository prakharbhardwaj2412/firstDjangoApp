from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
	"""docstring for StockSerializer"""
	class Meta(object):
		"""docstring for Meta"""
		model = Stock
		# to return some particular field as json
		# fields = ('ticker', 'volume')
		# to return all the fields
		fields = '__all__'