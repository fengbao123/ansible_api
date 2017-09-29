#!/usr/bin/env python
#encoding:utf-8

import ansible_api as aapi
import json

# ansible调用

# 主机列表: 可以是以IP的列表，也可以是组名
host_list = ['192.168.128.138','192.168.128.139']
#host_list = 'hostgroup2'
#host_list = ['hostgroup1','hostgroup2']


task_list = [
    dict(action=dict(module='shell',args='free -m')),
    dict(action=dict(module='ping')),
]
#task_list = [dict(action=dict(module='ping', args=None)),]

result = aapi.ansiblerun(host_list,task_list)

print task_list
print result

for host in host_list:
    print '='*100
    print  result[host]['stdout']

host_list = ['192.168.128.148','192.168.128.149']
result = aapi.ansiblerun(host_list,task_list)

for host in host_list:
    print '='*100
    print  result[host]['stdout']