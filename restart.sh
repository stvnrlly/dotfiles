#! /usr/bin/env bash

# OSX basics
# TODO: check what OS this is running on
sudo softwareupdate -i -a
xcode-select --install

# Install brew & brew-based utilities
# TODO: consider using coreutils
source ./install/brew.sh

# Install pip-based utilities
pyenv install 3.5.1
pyenv global 3.5.1
source ./install/pip.sh

# Install npm-based utilities
nodenv install 6.0.0
nodenv global 6.0.0
source ./install/npm.sh

# Install gem-based utilities
rbenv install 2.3.0
rbenv global 2.3.0
source ./install/gem.sh

# Set up terminal
## iTerm2
### settings
### colors
## oh my zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
## zsh
ln -s $(pwd)/configs/.zshrc ~/.zshrc
## custom prompt
mkdir ~/.oh-my-zsh/custom/themes
ln -s $(pwd)/configs/cloud.zsh-theme ~/.oh-my-zsh/custom/themes/cloud.zsh-theme 

# Set up text editor
## Atom
source ./install/apm.sh
## .vimrc

# Set up tmux
## .tmux.conf
## tmuxinator

# Symlink configs
## beets
## cmus
## lastfm

# Set up fonts
## Input
## Hack

# Set up connections to remote servers?

# Set up docker
