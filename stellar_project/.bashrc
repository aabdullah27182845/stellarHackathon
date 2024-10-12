export PYTHON_SYS_EXECUTABLE=$(which python3.12)
export PYTHONPATH=$(python3.12 -c "import sysconfig; print(sysconfig.get_paths()['purelib'])")
