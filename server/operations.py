import os
#import json

def register_node(instance_id,external_ip,hostname,hostgroup,template):
  f = open('/etc/nagios3/conf.d/' + instance_id + '.cfg','w')
  f.write('### Added by RegNagios System ###')
  f.write('define host {\n')
  f.write('	use		' + template.lower + '\n')
  f.write('	host_name	' + hostname.lower + '\n')
  f.write('	address		' + external_ip.lower + '\n')
  f.write('	hostgroups	' + hostgroup.lower + '\n')
  f.write('}')
  f.write('### ### ### ### ### ### ### ### ###')
  f.close()
  restart_nagios()

def deregister_node(instance_id):
  os.remove('/etc/nagios3/conf.d/' + instance_id + '.cfg')
  restart_nagios()

def restart_nagios():
  os.system('/etc/init.d/nagios3 reload')
