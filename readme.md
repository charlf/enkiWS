# enkiWS

## enki Web Services for Games on Python Google App Engine

A permissively licensed Python web service for games developers. enkiWS is a library for setting up a website and ancillary services for games on Google App Engine. GAE was chosen as the platform since it provides a low cost scalable solution.

Online demo - https://enkisoftware-webservices.appspot.com

## Status - version 0.1.0

This is a work in progress and not yet ready for production use.

## Functionality

### Current

* User Accounts - email, display name
* Login through OAuth & OpenID providers - Valve's Steam, Facebook, Google, Twitter
* Forums
* Localisation - English & French implemented

### Intended for release 1.0.0 

* Sales (Fastspring), game key generation, registration
* Friends
* Game API
  * Authentication (account and game key)
  * Multiplayer server list
  * Friends list & status
* Admin tools
* Installation and usage documentation

### Intended for  release 1.x.x

* User roles
* Issues reporting and tracking
* Static blogging tool integration
* Integration presskit for GAE, doDistribute, promoter

## Credits

Developed by [Juliette Foucaut](http://www.enkisoftware.com/about.html#juliette) - [@juliettef](https://github.com/juliettef)  
Architecture and OAuth implementation - [Doug Binks](http://www.enkisoftware.com/about.html#doug) - [@dougbinks](https://github.com/dougbinks)
Testing - Sven Bentlage - [@sbe-dev](https://github.com/sbe-dev)

## License

zlib - see [license.txt](https://github.com/juliettef/enkiWS/blob/master/license.txt)
