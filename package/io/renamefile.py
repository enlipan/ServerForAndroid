import os
import sys


def rename(path):
    file_name_suf = '-release.apk'
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            if "fengche" in filename:
                print filename
                os.rename(os.path.join(path, filename),
                          os.path.join(path, filename[filename.find("fengche"): len("fengche")] + file_name_suf))
            elif "chebaba" in filename:
                print filename
                os.rename(os.path.join(path, filename),
                          os.path.join(path, filename[filename.find("chebaba"): len("chebaba")] + file_name_suf))
            elif "jiehe" in filename:
                print filename
                os.rename(os.path.join(path, filename),
                          os.path.join(path, filename[filename.find("jiehe"): len("jiehe")] + file_name_suf))
            elif "fanglin" in filename:
                print filename
                os.rename(os.path.join(path, filename), os.path.join(path, filename[filename.find("fanglin"): len(
                    "fanglin")] + file_name_suf))
            elif "shenlong" in filename:
                print filename
                os.rename(os.path.join(path, filename),
                          os.path.join(path, filename[filename.find("shenlong"): len("shenlong")] + file_name_suf))
            elif "cadillac" in filename:
                print filename
                os.rename(os.path.join(path, filename),
                          os.path.join(path, filename[filename.find("cadillac"): len("cadillac")] + file_name_suf))
            elif "msld" in filename:
                print filename
                os.rename(os.path.join(path, filename),
                          os.path.join(path, filename[filename.find("msld"): len("msld")] + file_name_suf))
            elif "shangqi" in filename:
                print filename
                os.rename(os.path.join(path, filename),
                          os.path.join(path, filename[filename.find("shangqi"): len("shangqi")] + file_name_suf))
            elif "yingche" in filename:
                print filename
                os.rename(os.path.join(path, filename),
                          os.path.join(path, filename[filename.find("yingche"): len("yingche")] + file_name_suf))
            else:
                print filename + ' not recognize ... '


def list_path_files(path):
    rename(path)
    for f in os.listdir(path):
        abs_path = os.path.join(path, f)
        if os.path.isdir(abs_path):
            print "dir name is %s" % abs_path
            list_path_files(abs_path)
        elif os.path.isfile(abs_path):
            print "file name is %s" % abs_path


if __name__ == '__main__':
    for arg in sys.argv[1:]:
       print "input path name has : %s" % arg
       print "---------------------start open %s" % arg
       abspath = os.path.join(os.path.abspath("."), arg)
       print "input abs is %s" % abspath
       list_path_files(abspath)
    # list_path_files('/Users/paul/Documents/Release/archive')
