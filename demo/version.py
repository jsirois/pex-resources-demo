from pkg_resources import resource_string


def get_version():
    return str(resource_string('demo.version', 'version.txt')).strip()
