import random

from google.appengine.ext import ndb


class EnkiModelCounter( ndb.Model ):
# SHARDED COUNTER - https://cloud.google.com/appengine/articles/sharding_counters

	count = ndb.IntegerProperty( default = 0 )  # sharded counter

	@classmethod
	@ndb.transactional
	def increment( cls ):
		# Increment the value for a given sharded counter.
		NUM_SHARDS = 5
		shard_string_index = str( random.randint( 0, NUM_SHARDS - 1 ))
		counter = EnkiModelCounter.get_by_id( shard_string_index )
		if counter is None:
			counter = EnkiModelCounter( id = shard_string_index )
		counter.count += 1
		counter.put()

	@classmethod
	def get_count( cls ):
		# cumulative count of all sharded counters.
		total = 0
		for counter in EnkiModelCounter.query():
			total += counter.count
		return total