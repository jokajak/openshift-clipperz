This repository supports running the clipperz password-manager on Openshift.

##Limitations##
* No brute force protection
* No attachment support
* No bitcoin support

This should be used for personal use only.

Steps to set up:

1. rhc app create clipperz python-2.7 postgresql-9.2 --from-code https://github.com/jokajak/openshift-clipperz.git
2. rhc app start clipperz
