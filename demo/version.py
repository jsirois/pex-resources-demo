from pkg_resources import resource_string


def get_version():
    return resource_string('demo.version', 'version.txt').decode('utf-8').strip()
