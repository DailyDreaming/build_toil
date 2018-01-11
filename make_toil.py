import subprocess
import shlex
import os
import argparse
import textwrap


def heredoc(template, dictionary={}, indent=''):
    template = textwrap.dedent(template).format(**dictionary)
    return template.replace('\n', '\n' + indent) + '\n'

def write_bashscript(bash_string):
    with open('toil_script.sh', 'w') as f:
        f.write(bash_string)

def main():
    parser = argparse.ArgumentParser(description='Builds Toil from source.')
    parser.add_argument('-b', '--branch',
                        required=False,
                        default=None,
                        help='Branch to build.')
    args = parser.parse_args()

    if args.branch:
        bash_string = heredoc("""#!/usr/bin/env bash

        git clone https://github.com/BD2KGenomics/toil.git
        cd toil
        git checkout {branch}
        virtualenv venv
        . venv/bin/activate
        make prepare
        make develop extras=[aws,mesos,azure,google,encryption,cwl]
        """, {"branch": args.branch})

        branch_dir = './' + args.branch.split('/')[-1].replace(':', '')
        if not os.path.exists(branch_dir):
            try:
                os.makedirs(branch_dir)
                os.chdir(branch_dir)
            except:
                raise OSError('Could not create directory.')
        write_bashscript(bash_string)
        subprocess.check_call(shlex.split('sh toil_script.sh'))
    else:
        bash_string = heredoc("""#!/usr/bin/env bash

        git clone https://github.com/BD2KGenomics/toil.git
        cd toil
        virtualenv venv
        . venv/bin/activate
        make prepare
        make develop extras=[aws,mesos,azure,google,encryption,cwl]
        """)
        write_bashscript(bash_string)
        subprocess.check_call(shlex.split('sh toil_script.sh'))

if __name__ == '__main__':
    main()