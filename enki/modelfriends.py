from google.appengine.ext.ndb import model


class EnkiModelFriends( model.Model ):

	friends = model.IntegerProperty( repeated = True )  # couples of friends' Ids