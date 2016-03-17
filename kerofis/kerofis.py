#!/usr/local/bin
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      m.reboux
#
# Created:     01/2016
# Copyright:   (c) m.reboux 2015
# Licence:     <your licence>
#
#
# Documentation :
#	https://wiki.postgresql.org/wiki/Using_psycopg2_with_PostgreSQL
#	http://initd.org/psycopg/docs/usage.html#query-parameters
#	http://lxml.de/tutorial.html
#	http://apprendre-python.com/page-xml-python-xpath
# http://blog.paumard.org/cours/xml/chap02-premier-exemple-structure.html + http://www.w3schools.com/xml/xml_tree.asp
#
#-

#import psycopg2
#import pprint
#import encodings
#import codecs
#import traceback
#import string
import ConfigParser


# chaines de connexion aux bases de données
#sConnPostgre = "host='10.7.5.130' dbname='catalogue' user='gnadmin' password='gnadmin'"

# on lit le fichier de configuration
Config = ConfigParser.ConfigParser()
Config.read("config.ini")
# tests
#print Config
#print Config.sections()
print Config.get('test', 'FavoriteColor')

