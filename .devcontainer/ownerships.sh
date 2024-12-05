#!/bin/bash

# Varibale to store directory name
DIR_TO_CHANGE=/workspaces/rmr-projection-client-browser


# Move one dir up
cd ..

# Change user ownership from root to vscode
sudo chown -R vscode $DIR_TO_CHANGE

# Change group ownership from root to vscode
sudo chgrp -R vscode $DIR_TO_CHANGE

# Print message in terminal
echo "$DIR_TO_CHANGE Ownership successfully changed!"