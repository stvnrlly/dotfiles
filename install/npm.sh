#!/usr/bin/env bash

utils=(
  pa11y
  pa11y-reporter-1.0-json
  pageres-cli
)

npm install -g "${utils[@]}"
