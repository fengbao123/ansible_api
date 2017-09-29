#!/usr/bin/env python
#encoding:utf-8

import ansible_api2 as aapi
import json

# ansible调用

# 主机列表: 可以是以IP的列表，也可以是组名
host_list = ["192.168.128.138","192.168.128.139"]
#host_list = 'hostgroup2'
#host_list = ['hostgroup1','hostgroup2']


task_list = [
    dict(action=dict(module='shell',args='free -m')),
    dict(action=dict(module='shell',args='df -h')),
]
#task_list = [dict(action=dict(module='ping', args=None)),]

# order = 'free -m'
# result = aapi.run_adhoc("192.168.128.138",order)
#
# for i in result.host_ok:
#     print i
#
# result = aapi.run_adhoc("hostgroup1",order)
# print result.host_ok
#
# result = aapi.run_adhoc(host_list,order)
# for i in result.host_ok:
#     print '=' * 100
#     print i['ip']
#     print '=' * 18
#     print i['result']['stdout']
#
# print result.host_unreachable
# print result.host_failed

print '*' * 100

result = aapi.run_modules(host_list,task_list)
for i in result.host_ok:
    print '=' * 100
    print i['ip']
    print '=' * 18
    print i['result']['stdout']
