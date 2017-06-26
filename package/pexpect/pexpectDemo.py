# coding=utf-8
# coding = utf-8
import pexpect
import sys
import os
from subprocess import call

signBashShell = 'jarsigner -verbose -keystore fengche_keystore -signedjar {1}.apk  {0}  souche'


def signApkFile(inputFilePath, outputFilePath, passWord):
    shellStr = signBashShell.format(inputFilePath, outputFilePath)
    print shellStr
    proc = pexpect.spawn(shellStr)
    # 中英文环境
    index = proc.expect(['Enter Passphrase for keystore: ', '输入密钥库的密码短语: '])
    if index == 0:
        print 0
        proc.sendline(passWord)
    elif index == 1:
        print 1
        proc.sendline(passWord)
    else:
        print 'error'


def excuteCmd():
    print os.system('pwd')


def excutedCall():
    call(['ls', '-l'])


if __name__ == '__main__':
    print sys.argv[1:]
    # signApkFile(sys.argv[1:][0], sys.argv[1:][1])
