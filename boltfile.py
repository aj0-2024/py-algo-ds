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
