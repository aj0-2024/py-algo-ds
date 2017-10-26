"""
This file provides an easy way to run python specific tasks such as

code coverage:
-----------
>bolt coverage
"""
import bolt

bolt.register_task('coverage', ['shell.coverage'])

config = {
    'shell': {
        'coverage': {
            'command': 'py.test',
            'arguments': [
                '--cov-report',
                'term-missing',
                '--cov=src/',
                'tests/'
            ]
        }
    }
}
