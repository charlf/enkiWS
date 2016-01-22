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

## FAQ

### Why use Google App Engine?

Small games developers like ourselves typically have very irregular backend requirements - website and service traffic are typically relatively low, but spike when there's a new release or if some content goes viral. Google App Engine (GAE) provides a low cost scalable solution for this scenario. For more information see our article on [Implementing a static website in Google App Engine](http://www.enkisoftware.com/devlogpost-20130823-1-Implementing_a_static_website_in_Google_App_Engine.html) or [Wolfire's article on GAE for indie developers](http://blog.wolfire.com/2009/03/google-app-engine-for-indie-developers/) as well as [Wolfire's article on hosting the Humble Indie Bundle](http://blog.wolfire.com/2010/06/Hosting-the-Humble-Indie-Bundle-on-App-Engine).

### Why Python?

Python is sufficiently popular and easy to use that it made a convenient choice of language from those available on Google App Engine. We considered Google's Go language, but although it has many benefits we thought it would be less widely known in the game development community.

## Credits

Developed by [Juliette Foucaut](http://www.enkisoftware.com/about.html#juliette) - [@juliettef](https://github.com/juliettef)  
Architecture and OAuth implementation - [Doug Binks](http://www.enkisoftware.com/about.html#doug) - [@dougbinks](https://github.com/dougbinks)  
Testing - Sven Bentlage - [@sbe-dev](https://github.com/sbe-dev)

## License

zlib - see [license.txt](https://github.com/juliettef/enkiWS/blob/master/license.txt)
