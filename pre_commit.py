import os
import subprocess

from typing import List

import mypy.main
import pylint.lint


def main() -> None:
    changed_py_files = subprocess.getoutput('git diff --name-only --staged "*.py"').splitlines()
    lint_changed_py_files(changed_py_files)
    static_type_check_packages_and_modules(changed_py_files)


def lint_changed_py_files(
    changed_py_files: List[str]
) -> None:
    config_path    = os.path.join('', '.pylintrc')
    pylint_options = f'--rcfile={config_path}'
    for changed_py_file in changed_py_files:
        # pylint.run_pylint(pylint_options + [changed_py_file])
        # # calls pylint.lint.Run(argv or sys.argv[1:])
        # # but does not allow specifying the reporter, exit, do_exit
        # # arguments to pylint.lint.Run.__init__
        pylint.lint.Run(args=[pylint_options, changed_py_file], exit=False)


def static_type_check_packages_and_modules(
    changed_py_files: List[str]
) -> None:
    # the pre-commit-nix file located in ./.git/hooks/pre-commit
    # calls this (pre_commit.py) module from the test_project
    # directory, so this module needs to move into the
    # test_project/python directory in order to find the
    # test_project_python and test_project_python_tests packages
    mypy_flags = [
        '--strict',
        '--show-error-context',
        '--show-column-numbers',
        '--show-error-end',
        '--pretty',
        '--show-absolute-path'
    ]
    package_configs = [
        # ['-p', '2020'], # ignore for now
        ['-p', '2024'],
    ]
    for package_config in package_configs:
        current_config = mypy_flags + package_config
        print(f'''mypy {' '.join(current_config)}''')
        mypy.main.main(args=current_config, clean_exit=True)
    for changed_py_file in changed_py_files:
        current_config = mypy_flags + [changed_py_file]
        print(f'''mypy {' '.join(current_config)}''')
        mypy.main.main(args=current_config, clean_exit=True)


if __name__ == '__main__':
    main()
