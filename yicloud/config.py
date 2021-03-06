# -*- coding: utf-8 -*-
import os

class DefaultConfig(object):
    PROJECT = "YiCloud"
    DEBUG   = False
    TESTING = False
    #http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'tanyang'
    #Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
    SQLALCHEMY_ECHO = True
    #MYSQL for production
    #SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db?charset=utf8'
    #Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60
    
    #VM config
    hostUri = 'qemu+ssh://tanyang@localhost/system'
    XMLPath = '/home/tanyang/yicloud/virtscripts/yivm1.xml'
    XMLOutput = '/home/tanyang/yicloud/virtscripts'
