#!/usr/bin/env python

import argparse
from glob import glob
from tempfile import mkdtemp
from subprocess import Popen, PIPE 


def exec_command(cmd_args):
    proc = Popen(cmd_args, stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = proc.communicate()
    res = proc.wait():
    return (res, stdout, stderr)

def main():
    parser = argparse.ArgumentParser(description='IUS QA Test')
    # nothing to do here yet

    
    for spec in glob('./specs/*.spec'):
        pkg = os.path.basename(spec).split('-qa-')[0]
        
        
        cmdargs = [
            'mock', '-r', 'ius-5-x86_64', 
            '--buildsrpm', 
            '--specfile=%s' % spec,
            "--sources='.'"
            ]
        (res, stdout, stderr) = exec_command(cmdargs)

        
        print stdout

        cmdargs = ['mock', '-r', 'ius-5-x86_64', 'rebuild', srpm]
        (res, stdout, stderr) = exec_command(cmdargs)
        cmdargs = ['mock', '-r', 'ius-5-x86_64', 'rebuild', srpm]
        (res, stdout, stderr) = exec_command(cmdargs)

if __name__ == '__main__':
    main()

