from google.appengine.ext.ndb import model


class EnkiModelTokenAuth( model.Model ):

	token = model.StringProperty() # unique
	user_id = model.IntegerProperty() # the ndb ID nr
	time_created = model.DateTimeProperty( auto_now_add = True )

