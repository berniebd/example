# -*- encoding:utf-8 -*-
import paramiko

__author__ = 'bida'


class SshOperator:
    def __init__(self):
        pass

    @staticmethod
    def execute_remote_ssh(connect_info, command):
        """
        执行远程ssh命令
        :param connect_info:远程主机连接信息
        :param command:
        """
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(connect_info['host'], connect_info['port'], connect_info['username'], connect_info['password'],
                           connect_info=5)

            stdin, stdout, stderr = client.exec_command(command)

            for std in stdout.readlines():
                print std

            client.close()
        except Exception, e:
            print e
