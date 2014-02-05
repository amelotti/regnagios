#!/usr/bin/python

import operations
#import json
from bottle import route, run, request

#insert a new node
@route('/nagios/register', method='POST')
def post():
  instance_id = request.forms.get('instance_id')
  external_ip = request.forms.get('external_ip')
  hostname = request.forms.get('hostname')
  hostgroup = request.forms.get('hostgroup')
  template = request.forms.get('template')
  operations.register_node(instance_id,external_ip,hostname,hostgroup,template)
  return { "success" : True }

#remove a node
@route('/nagios/register', method='DELETE')
def delete():
  instance_id = request.forms.get('instance_id')
  operations.deregister_node(instance_id)
  return { "success" : True }

run(host="0.0.0.0")
