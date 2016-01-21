import urllib
import urlparse
import jinja2

import enki


@jinja2.contextfilter
def make_local_url( context, route_name = 'home', parameters = {} ):
	return enki.libutil.make_local_url( context[ 'locale' ], route_name, parameters )


def join_url_param_char( input_url, parameters = {} ):
	output_url = input_url
	# add or modify parameters in a url
	if parameters:
		# replace the parameter values of the url with the corresponding values in the dictionary
		# parse the input url
		parsed_url= urlparse.urlparse( output_url )
		# if the original url had a query, update it with the input parameters
		parsed_url_query = {}
		if parsed_url.query:
			parsed_url_query = dict( urlparse.parse_qsl( parsed_url.query, keep_blank_values = True )) # note: can't handle multiple values for the same key
		parsed_url_query.update( parameters )
		# turn the parsed url result into a list, update it with the new query parameters (encoded)
		parsed_url_list = list( parsed_url )
		parsed_url_list[ 4 ] = urllib.urlencode( parsed_url_query )
		# build the new url with the updated parameters
		output_url = urlparse.urlunparse( parsed_url_list )
	return output_url
