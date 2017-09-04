0.7

* Add app: Mastodon
* Add app: Nextcloud
* Allow uploads of over 2M in proxy
* Remove Forum for simplicity

0.6

* Add apps: Tiny Tiny RSS, wallabag, Piwik
* Fix look of various pages on mobile
* Support application version to prepare for application upgrade
* Application stats and list commands
* Simplify deployment
* Update various apps and fix various bugs
* Manual migration: Run 'app init_running' command to update table with currently running apps

0.5

* Convert docker-compose.yml files to version 2, new networking, volumes
* Email support in all Apps
* Get rid of App manifest.yml file, use README.md instead
* Create puffinrocks organisation on Github on Dockerhub, move all projects there
* Separate Apps into independent repositories - allows automatic image generation and maintenance
* Dnsmasq for easier development
* Always use docker images instead of building
* Update example Compose file
* puffin.rocks usability improvements (simple stats, OpenGraph)
* Various bugfixes

0.4

* Add Flarum forum app, configure as Puffin forum
* Application screenshots
* List of user applications
* Allow to disable registration and emails
* Always create default Puffin user
* Single and multiple Puffin installation config and description
* Rewrite user and update developer documentation

0.3

* Application settings, custom domain
* User profile, change password
* Allow building dependencies to use optimized images
* Preserve volumes between restarts via data-only containers
* Add Gogs Git hosting app
* Handle signals via dumb-init, graceful shutdown
* Application presentation, website, subtitle
* Start, stop and other icons
* Main menu links
