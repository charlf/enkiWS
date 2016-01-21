from google.appengine.ext.ndb import model


class EnkiModelDisplayName( model.Model ):

	user_id = model.IntegerProperty()
	prefix = model.StringProperty() # prefix e.g. 'Jane'
	suffix = model.StringProperty() # suffix e.g. '#1234' => full display name = 'Jane#1234'
	current = model.BooleanProperty( default = True )
	time_created = model.DateTimeProperty( auto_now_add = True )
