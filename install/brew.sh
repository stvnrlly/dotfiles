
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap homebrew/versions
brew tap caskroom/fonts

basics = (
  git
  zsh
  zsh-completions
  nodenv
  pyenv
  pyenv-virtualenvwrapper
  rbenv
  tmux
  tldr
  curl
  sqlite
  postgresql
  mysql
  redis
  jq
  keybase
  pandoc
  imagemagick
  clamav
  mongodb
  httpie
  wget
  gnu-tar
  diff-so-fancy
  gifsicle
  hub
  cmus
  tree
  sox
  spark
  cowsay
  unpaper
  htop
  youtube-dl
  ffmpeg
  fdupes
  tmuxinator-completion
  watch
  t-completion
  exercism
  syncthing
)

docker = (

)

apps = (
  atom
  firefox
  iterm2
  flux
  slack
)

fonts = (
  font-input
  font-hack
)

brew install "${basics[@]}"
# TODO: figure out the docker stuff
# brew install "${docker[@]}"
brew cask install "${apps[@]}"
brew cask install "${fonts[@]}"
