#!/usr/bin/python3

import os
import paramiko

SRVRS = [{'ip':'10.10.2.3', 'un':'bender'}, {'ip':'10.10.2.4', 'un':'fry'}]
CMDLIST = ['touch sshworked.txt', 'touch sshworked2.txt', 'uptime']

def cmdissue(sshsession, commandtoissue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(commandtoissue)
    return ssh_stdout.read()



def main():
    # harvest RSA key (ssh priv key)
    myprivkey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    for server in SRVRS:
        #init connection to remote machine
        sshsession = paramiko.SSHClient()
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshsession.connect(hostname=server['ip'], username=server['un'], pkey=myprivkey)

        
        # init connection to remote machine

        # touch two files

        # get uptime of server
        for commandtoissue in CMDLIST:
            with open("serverresults.log", "a") as svrlog:
                print(cmdissue(sshsession, commandtoissue), file=svrlog)


        # close connection
        sshsession.close()

if __name__ == '__main__':
    main()

