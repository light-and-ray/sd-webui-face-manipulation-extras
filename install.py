import launch

if not launch.is_installed('dlib-bin'):
    launch.run_pip('install dlib-bin')
