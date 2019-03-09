sections = {
    'cs-basics': {
        'heading': 'CS Basics',
        'subsections': {
            'oops': 'OOPS',
            'web_dev': 'Web Development',
            'compilers': 'Interpreter vs Compilers',
            'quick_rems': 'Quick Remembers',
            'data_structures': 'Data Structures'
        }
    },
    'cs-course': {
        'heading': 'CS Course',
        'subsections': {}
    },
    'php': {
        'heading': 'PHP',
        'subsections': {
            'common': 'Common',
            'slim': 'SLIM',
            'yii': 'YII2'
        }
    },
    'node': {
        'heading':  'Node',
        'subsections': {
            'basic': 'BASICS',
            'event_loop': 'Event Loop',
            'blocking_unblocking': 'Blocking vs Non-Blocking',
        }
    },
    'angular': {
        'heading': 'ANGULAR',
        'subsections': {
            'basic': 'BASICS'
        }
    },
    'sde': {
        'heading':  'Software Development',
        'subsections': {}
    },
    'networking': {
        'heading': 'Network Basics',
        'subsections': {}
    },
    'coding': {
        'heading': 'Coding Questions',
        'subsections': {
            'algos': 'Algorithms & Implementations',
            'arrays': 'Arrays',
            'algo_analysis': 'Analysis of Algorithms'
        }
    },
    'interview-exp': {
        'heading': 'Interview Experiences',
        'subsections': {}
    },
    'databases': {
        'heading': 'Databases',
        'subsections': {}
    },
    'gk': {
        'heading': 'GK',
        'subsections': {}
    },
    'python': {
        'heading': 'Python',
        'subsections': {
            'flask': 'Flask'
        }
    },
    'docker': {
        'heading': 'Docker',
        'subsections': {
            'basics': 'Basics'
        }
    }

}


def getSecHeading(sec) :
    return sec.heading


sectionNames = map(getSecHeading, sections)
