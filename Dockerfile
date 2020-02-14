FROM fluentd:latest
USER root

RUN apk --no-cache --update add \
                            build-base \
                            ruby-dev && \
    gem install fluent-plugin-mongo && \
    apk del build-base ruby-dev && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

RUN apk --no-cache add bind-tools
COPY ./fluent.conf /fluentd/etc/


