FROM node:22
# Install basic development tools
RUN \
     apt update && \
     apt install -y less man-db sudo vim jq python-is-python3 python3-virtualenv tini pgloader \
     inetutils-ping inetutils-telnet postgresql-client locales

RUN \
    VER=0.19.21 ;\
    ARCH=$(dpkg --print-architecture) ;\
    curl -sL https://github.com/xo/usql/releases/download/v$VER/usql_static-$VER-linux-$ARCH.tar.bz2 | tar xjvf  - usql_static  ;\
    mv usql_static /usr/bin/usql 

# Ensure default `node` user has access to `sudo`
ARG USERNAME=node
RUN \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# install ops and plugins
USER node
RUN \
    curl -sL https://bit.ly/get-ops | bash
ENV PATH="/home/node/.local/bin:${PATH}"
RUN \
    ops -update
RUN \
    ops -plugin https://github.com/mastrogpt/olaris-ai ;\
    ops ai

ENTRYPOINT ["tini", "--"]
CMD ["sleep", "infinity"]
