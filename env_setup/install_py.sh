#!/bin/sh

# Installing pyenv
yum install -y --skip-broken git gcc zlib-devel bzip2-devel readline-devel sqlite-devel
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec $SHELL
pyenv install 3.7.6
pyenv versions
pyenv shell 3.7.6
python --version
pip3.7 install --upgrade pip
