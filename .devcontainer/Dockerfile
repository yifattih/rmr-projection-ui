FROM mcr.microsoft.com/devcontainers/base:bullseye

ARG USERNAME=vscode

# install jless (because its not available at https://containers.dev/features at time of writing)
RUN NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" \
        && (echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> /home/vscode/.profile \
        && eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)" \
        && brew install jless
