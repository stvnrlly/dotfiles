export PATH=$PATH:~/.local/bin

eval "$(pyenv init -)"

export NVM_DIR="$HOME/.nvm"

eval "$(starship init zsh)"

# activate syntax highlighting
source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# activate fancier history search
source /opt/homebrew/share/zsh-history-substring-search/zsh-history-substring-search.zsh
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down
