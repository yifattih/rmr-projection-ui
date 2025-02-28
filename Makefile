## ============================================================================
##          Inspired on https://github.com/thevops/makefile-automation
##          Additions by: @yifattih
##          Description: Makefile for common DevOps and software
##                       development taks automation
## ============================================================================

#  Check if the version of Make is 4.3
NEED_VERSION := 4.3
$(if $(filter $(NEED_VERSION),$(MAKE_VERSION)),, \
 $(error error You must be running make version $(NEED_VERSION).))

# By default Makefile use tabs in indentation. This command allow to use SPACES
# .RECIPEPREFIX +=                      # Make Version < 4.3
.RECIPEPREFIX := $(.RECIPEPREFIX)       # Make Version = 4.3

# By default every line in every task in ran in separate shell.
.ONESHELL:                              # Run all commands in a single shell

# By default Makefile use /bin/sh
SHELL:=/bin/bash

# It enables exiting if there will be error in pipe, eg. something | command | something_else
.SHELLFLAGS := -eu -o pipefail -c

# Optionally load env vars from .env
# include .env

ARGS = $(filter-out $@,$(MAKECMDGOALS))
ARG1 := $(word 2, $(ARGS))
ARG2 := $(word 3, $(ARGS))
ARG3 := $(word 4, $(ARGS))
ARG4 := $(word 5, $(ARGS))
ARG5 := $(word 6, $(ARGS))

# -----------------------------   DO NOT CHANGE   -----------------------------
help:
    @ grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) \
        | sed -e 's/^.*Makefile://g' \
        | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' \
        | sed -e 's/\[32m##/[33m/'
    @ echo

# Prevents make from treating arguments as targets
%:
    @:

.DEFAULT_GOAL := help

include mkModules/colors.mk
include mkModules/cans.mk
include mkModules/git.mk
include mkModules/service.mk
