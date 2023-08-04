#! /bin/bash

# pygame依赖的库
brew install hg sdl sdl_image sdl_ttf

# 声音
brew install sdl_mixer portmidi

# pygame
# 书上：pip3 install --user hg+http://bitbucket.org/pygame/pygame
# 书上的没用。
# 解决方法：
# conda create -y -n py3.6 python=3.6
# conda activate py3.6
pip install pygame




