#!/usr/bin/env bash

utils=(
  autocomplete-python@1.8.12
  autocomplete-ruby@0.2.3
  color-picker@2.2.3
  cucumber@0.5.0
  git-time-machine@1.5.4
  increment-selection@0.3.0
  linter@1.11.18
  linter-csslint@1.3.3
  linter-jade@0.3.2
  linter-jshint@3.0.1
  linter-jsonlint@1.3.0
  linter-python-pep8@0.2.0
  linter-rubocop@0.5.0
  markdown-scroll-sync@2.1.2
  merge-conflicts@1.4.4
  minimap@4.25.6
  pretty-json@1.6.1
  sort-lines@0.14.0
  tabs-to-spaces@1.0.2
  travis-ci-status@1.3.0
)

apm install "${utils[@]}"
