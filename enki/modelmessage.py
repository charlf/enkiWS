from google.appengine.ext.ndb import model


class EnkiModelMessage( model.Model ):

	sender = model.IntegerProperty()
	recipient = model.IntegerProperty()
	type = model.StringProperty( choices = [ 'friend_request' ] )
	time_created = model.DateTimeProperty( auto_now_add = True )