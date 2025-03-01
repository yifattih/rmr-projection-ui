#-----------------------------------------------------------------------------#
##
##-----------------------------------------------------------------------------
##|                          Git Targets                                      |
##-----------------------------------------------------------------------------
##
#-----------------------------------------------------------------------------#
.PHONY: gst glog gc gcd gp gbr gbrn gbrp gbrd gbrw

gst: ## Show a git status glimpse
##  |Usage:
##  |   $ make status
##
    @ echo
    @ $(call headercan,"SUMMARY --- FILES CHANGES")
    @ changes="$(shell git add -N . && git diff --color --stat HEAD | sed '$d; s/^ //')"
    @ if [ -z "$$changes" ]; then \
        $(call inform,"No file changes!") \
		&& echo \
		&& exit 0; \
    else \
		for file in $(shell git status -s | grep "^..* " | sed "s/^.. //g"); do git diff --color --stat HEAD "$$file" | sed '$d; s/^ //' | head -n 1; done; \
		git reset . --quiet
    fi
    @ echo

glog: ## Displays a Git log in a user-friendly format following the Conventional Commits standard
# 	---------------
##  |USAGE:
##  |   $ make log <entries>
# 	---------------
##	|Parameters:
##	|	entries: integer | default = 5
# 	|		Number of entries to display
##
    @ echo
    @ $(call headercan,"COMMITS")
    @ # Script
    if [ -z "$(ARG1)" ]; then \
		git --no-pager log -n 5 --abbrev-commit --format=format:"%s-- " \
		| sed "s/-- /\n/g" \
		| sed -r \
		-e 's/([^(:]*)(\([^)]*\))(:)(.*)/$(call COMMITFORMAT)/g' \
		| tac; \
		echo; \
    elif ! echo "$(ARG1)" | grep -qE '^[0-9]+$$'; then \
        $(call err,"Number of entries must be an integer!!!")
        while true; do \
            $(call prompt,"How many entries?"); \
            if ! echo "$$input" | grep -qE "^[0-9]+$$"; then \
                $(call err,"Must be an integer!!!") \
                && echo; \
            else \
                echo; \
                git --no-pager log -n "$$input" --abbrev-commit --format=format:"%s-- " \
                | sed "s/-- /\n/" \
                | sed -r \
                -e 's/([^(:]*)(\([^)]*\))(:)(.*)/$(call COMMITFORMAT)/g' \
                | tac; \
                echo; \
                exit 0; \
            fi; \
        done; \
    else \
        git --no-pager log -n "$(ARG1)" --abbrev-commit --format=format:"%s-- " \
		| sed "s/-- /\n/" \
        | sed -r \
        -e 's/([^(:]*)(\([^)]*\))(:)(.*)/$(call COMMITFORMAT)/g' \
        | tac; \
    fi;
    @ echo

gc: ## Stage files, prepare and execute cit
##  |Usage:
##  |   $ make gcommmit
##
    @ is_change="$(shell git status --porcelain | sed "s/.* //")"
    @ if [ -z "$$is_change" ]; then \
		echo \
        && $(call inform,"No files to commit!!!"); \
        echo; \
        exit 0; \
	fi
    @ $(MAKE) --silent gst
    $(call headercan,"ENTER NUMBER OF FILE")
    @ select filename in $(shell git status -s | cut -c4- && echo "." && echo "Exit"); do \
		if [[ "$$filename" == "Exit" ]]; then \
			echo \
			&& $(call inform,"Commit canceled!") \
			&& echo \
			&& exit 0; \
		fi; \
		echo; \
		if [[ "$$filename" == "." ]]; then \
			echo \
			&& $(call keyvaluecan,"Staged","All") \
			&& git add . \
			&& break; \
		fi; \
		echo; \
		if [[ -n "$$filename" ]]; then \
			$(call keyvaluecan,"Staged",$$filename) \
			&& git add $$filename \
			&& break; \
		else \
			$(call err,"Invalid selection"); \
		fi; \
	done
    @ echo
    @ $(call headercan,"COMMIT MESSAGE")
    @ $(call inform,"Message construction based on the AngularJS commit convention")
    @ while true; do \
        $(call prompt,"Type") && type="$$input"; \
        if [ "$$type" == "exit" ]; then \
            $(call inform,"Unstaging files"); \
            git restore --stage .; \
            $(call inform,"Commit canceled!") \
            && echo \
            && exit 0; \
        elif [ "$$type" == "" ]; then \
            $(call err,"The Type field cannot be empty"); \
        else \
            $(call inform,"Type field stored"); \
            $(call keyvaluecan,"Type","$$type") \
            && break; \
        fi;
    done;
    @ echo
    @ while true; do \
        $(call prompt,"Scope") && scope="$$input"; \
        if [ "$$scope" == "exit" ]; then \
            $(call inform,"Unstaging files"); \
            git restore --stage .; \
            $(call inform,"Commit canceled!") \
            && echo \
            && exit 0; \
        elif [ "$$scope" == "" ]; then \
            $(call err,"The Scope field cannot be empty"); \
        else \
            $(call inform,"Scope field stored"); \
            $(call keyvaluecan,"Scope","$$scope") \
            && break; \
        fi;
    done;
    @ echo
    @ while true; do \
        $(call prompt,"Imperative Description") && description="$$input"; \
        if [ "$$description" == "exit" ]; then \
            $(call inform,"Unstaging files"); \
            git restore --stage .; \
            $(call inform,"Commit canceled!") \
            && echo \
            && exit 0; \
        elif [ "$$description" == "" ]; then \
            $(call err,"The Description field cannot be empty"); \
        else \
            $(call inform,"Description field stored"); \
            $(call keyvaluecan,"Description","$$scope") \
            && break; \
        fi;
    done;
    @ echo
    @ $(call headercan,"COMMIT SUMMARY")
    @ message=""$$type"("$$scope"): "$$description"" 
    @ $(call keyvaluecan,"Filename")
    @ echo "$$filename"
    @ $(call keyvaluecan,"Message")
    @ echo -e "$$message"
    @ echo
    @ git commit -m "$$message"
    @ $(call inform,"Done!")
    @ echo

gcd: ## Delete last commit message
##  |Usage:
##  |   $ make gcommd
##
    @ echo
    @ $(call headercan, "DELETE LAST COMMIT")
    @ hash="$(shell git rev-parse --short HEAD)"
    @ $(call keyvaluecan,"Hash",$$hash)
    @ git reset --soft HEAD~1
    @ echo

gbr: ## Prints Git branches
##  |Usage:
##  |   $ make gbr
##
    @ echo
    @ CURRENT+="$(shell git branch --show-current)"
    @ LOCAL+="$(shell git branch --format="%(refname:short)")"
    @ REMOTE+="$(shell git branch -r --format="%(refname:short)" | sed "s/origin\///g")"
    @ $(call headercan,"BRANCHES")
    @ $(call keyvaluecan,"Current",$$CURRENT)
    @ $(call keyvaluecan,"Local",$$LOCAL)
    @ $(call keyvaluecan,"Remote",$$REMOTE)
    @ echo


gbrn: ## Create a new branch
##  |Usage:
##  |   $ make gbrn <string: branch name>
##
    @ echo
    @ $(call headercan,"NEW BRANCH")
    @ while true; do \
		$(call prompt,"Branch name") && branch="$$input"; \
		if [ "$$branch" == "exit" ]; then \
			$(call inform,"Branch creation canceled!") \
			&& echo \
			&& exit 0; \
		elif [ "$$branch" == "" ]; then \
			$(call err,"Branch name cannot be empty!"); \
		else \
			git checkout -b "$$branch"; \
			$(call inform,"Branch $$branch created!") \
			&& echo \
			&& exit 0; \
		fi; \
	done;
    @ echo

gbrp: ## Push current branch to remote
##  |Usage:
##  |   $ make gbrp
##
    @ echo
    @ $(call headercan,"PUSH BRANCH")
    @ branch="$(shell git branch --show-current)"
    @ $(call keyvaluecan,"Branch",$$branch)
    @ git push --set-upstream origin $$branch
    @ echo