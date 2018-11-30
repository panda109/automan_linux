'''
Created on 2010/12/20


0 Mon Dec 20 15:36:05 2010
0 Mon Dec 20 15:36:08 2010
0 Mon Dec 20 15:36:10 2010
1 Mon Dec 20 15:36:12 2010
0 Mon Dec 20 15:36:14 2010
0 Mon Dec 20 15:36:16 2010

@author: panda.huang
'''
#   <?xml version="1.0" encoding="US-ASCII"?>
#    <testsuite tests="2" time="" failures="1" error="0" name="[09-07][16-44-18][device_list_1]]">
#      <testcase time="0.0 sec" result="fail" name="test_db_1">
#        <failure message="FAIL !!"/>
#      </testcase>
#      <testcase time="2.0 sec" result="pass" name="test_db">
#      </testcase>
#    </testsuite>
import pexpect
import requests
if __name__ == '__main__':
    child = pexpect.spawn('ssh root@172.24.110.28')
    fout = file('./log/mylog.txt','w') 
    child.logfile = fout 
    child.expect('password:')
    child.sendline('111111')
    child.expect('Password:')
    key = ""
    f = open('./log/mylog.txt','r') 
    for line in f.readlines():
        #line = f.readline()
        if line[0] == "$":
            key = line[2:] 
    f.close()
    payload = {'original_string': key}
    r = requests.post("http://swd.infortrend/linux_login_util.py", data=payload)
    for line in r.text.splitlines():
        if "Result" in line :
            key =   line[34:42]
            print key
    child.sendline(key)
    child.expect('# ') 
    #print child.before
    #print child.after
    child.sendline("ls")
    child.expect(".cfg")
    child.close(force=True)

#define
#testsuite

#testcase time result name
#failure message

#testsuite