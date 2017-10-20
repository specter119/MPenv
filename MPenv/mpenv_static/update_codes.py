#!/usr/bin/env python
import os
import subprocess

def update_code():
    subprocess.check_call('git pull', shell=True, executable="/bin/bash")
    subprocess.check_call('pip install -e .', shell=True, executable="/bin/bash")

if __name__ == '__main__':
    db_loc = os.environ['DB_LOC']
    env_loc = os.path.dirname(os.path.dirname(db_loc))
    codes_loc = os.path.join(env_loc, 'codes')

    for d in os.listdir(codes_loc):
        m_dir = os.path.join(codes_loc, d)
        print('changing to {}'.format(m_dir))
        print('updating {}'.format(d))
        os.chdir(m_dir)
        update_code()


