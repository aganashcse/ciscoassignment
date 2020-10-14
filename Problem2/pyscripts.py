"""
This python code has scripts to execute some commands in remote server through SSH
"""
from scp import SCPClient, SCPException
import paramiko
from telnetlib import Telnet

# ----------------------------------------------------------------#
# ----------------------------------------------------------------#
# Question 1:
# ----------------------------------------------------------------#


def telnet_method():
    with Telnet('localhost', "999") as tn:
        tn.write("hello world!\n")

        print(tn.read_all())
# ----------------------------------------------------------------#


def ssh_connect():
    host = "<<ip>>"
    port = 22
    username = "user"
    password = "passwd"

    ls_command = "ls"
    disk_usage_cmd = "df -h"
    inode_count_cmd = "find . | wc -l"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
# below is the way to connect if we have privatekey file
# # # ssh.connect(host, port, username, password='',
# # #             key_filename='C://Users//Ganesh//Desktop//gcp_privatekey.ppk')


def execute_cmd(cmd="ls", ssh):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    lines = stdout.readlines()
    print("output:\n", lines)


def sftp_method(ssh):
    sftp = ssh.open_sftp()
    sftp.put("C://Users//Ganesh//Desktop//a.txt",
             "//home//s_rajkumar1980//ab.txt")
    sftp.close()


def close_ssh_connection(ssh):
    ssh.close()

# ----------------------------------------------------------------#
# SCP


def scp_method(shh):
    scp = SCPClient(ssh.get_transport())
    scp.put(
        "C://Users//Ganesh//Desktop//a.txt",
        recursive=True,
        remote_path="//home//s_rajkumar1980//ab.txt"
    )
    scp.close()


# ----------------------------------------------------------------#
# ----------------------------------------------------------------#
# Question 2:
# ----------------------------------------------------------------#
telnet_method()  # to iniate telnet context
# execution of below commands aids in creating n files(default to 10)
# NUM=${1:-10}   ## default to 10 files
# SIZE=${2:-666} ## default to 666 bytes
# n=0
# while [ $n -lt $NUM ]
# do
#   printf "%0${SIZE}d" 0 > "FILE$n"
#   n=$(( $n + 1 ))
# done

# to zip and unzip the files, we can use zip, unzip tools in linux
# zip file_name_to_zip
# unzip zipped_file_name are the commands to compress and extract the files

# ----------------------------------------------------------------#
# ----------------------------------------------------------------#
# Question 3:
# ----------------------------------------------------------------#


# ----------------------------------------------------------------#
# ----------------------------------------------------------------#
# Question 4:
# ----------------------------------------------------------------#
# server commands
# top = command to observe which process occupies how much load
# i - to show except idle tasks
# M – sort task list by memory usage
# P – sort task list by processor usage
# N – sort task list by process ID
# T – sort task list by run time

# ----------------------------------------------------------------#
# ----------------------------------------------------------------#
# Question 5, 6:
# ----------------------------------------------------------------#

# sql commands
# create view temp_view as select * from routers limit 10;

# insert into table_name select ip, host, '1' type from table_name where <cond>
