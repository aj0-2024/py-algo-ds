"""
This file provides an easy way to run python specific tasks such as

code coverage:
-----------
>bolt coverage
"""
import bolt

bolt.register_task('coverage', ['shell.coverage'])
bolt.register_task('test', ['shell.test'])

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
        },
        'test' : {
            'command': 'py.test',
            'arguments': [
                '-x'
            ]
        }
    }
}
