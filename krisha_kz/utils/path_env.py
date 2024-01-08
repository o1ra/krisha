import os


def get_env_path(env):
    main_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path_env = os.path.join(main_path, 'tests', 'ui', f'.env.{env}')
    return path_env
