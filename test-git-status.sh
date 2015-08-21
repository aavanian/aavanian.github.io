#!/usr/bin/env bash
if [[ -n $(git status -s) ]]; then echo >&2 "git status not clean"; exit 1; fi
