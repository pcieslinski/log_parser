from collections import namedtuple


LogLine = namedtuple(
    'LogLine',
    [
        'prefix',
        'host',
        'identity',
        'user',
        'date',
        'request',
        'status',
        'bytes',
        'referer',
        'user_agent'
    ]
)
