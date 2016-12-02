if [[ -z $ZSH_THEME_CLOUD_PREFIX ]]; then
    ZSH_THEME_CLOUD_PREFIX='☁'
fi

export VIRTUAL_ENV_DISABLE_PROMPT=true
PROMPT='%{$fg_bold[cyan]%}$ZSH_THEME_CLOUD_PREFIX %{$fg_bold[green]%}%p %{$fg[green]%}%c %{$fg_bold[cyan]%}$(git_prompt_info)%{$fg_bold[blue]%} % %{$reset_color%}'
RPROMPT='%{$fg_bold[cyan]%}$(get_virtual_env)%{$reset_color%}'

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[green]%}[%{$fg[cyan]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[green]%}] %{$fg[yellow]%}⚡%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[green]%}]"

get_virtual_env() {
  if [[ -n $VIRTUAL_ENV ]]; then
    echo "[🐍 :$(basename $VIRTUAL_ENV)]"
  fi
}
