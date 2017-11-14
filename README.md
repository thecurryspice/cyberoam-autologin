# cyberoam-auto-login

Some simple Python scripts to work on Cyberoam networks

### Features

* Auto-Login from given choices
* Scan all possible usernames with a default password
* Auto-Connect on network dropouts

### Issues

* Uninterrupted Download Manager (udm) is *practically useless*:
	* Doesn't work for intranet systems with pinging disabled.
	* Cannot detect forbidden ports, or detect open ports and use them for checking connection
	* Will get stuck in login loop due to above reasons

### Idea List
* Linking *scanner* and *login* scripts. Output of *scanner* can be stored in a file which feeds *login* script
