FROM nginx:1.17.8

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install pymongo
RUN mkdir /etc/kub_logs
COPY ./extracter.py /etc/
COPY ./entrypoint.sh /etc/
RUN mkdir /etc/kub-logs
COPY ./default.conf /etc/nginx/conf.d/
CMD ["/etc/entrypoint.sh"]
RUN chmod u+x /etc/entrypoint.sh
