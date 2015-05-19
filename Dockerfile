FROM phusion/baseimage:0.9.16

RUN sudo apt-get update
RUN sudo apt-get install -y python
RUN sudo apt-get install -y python-requests

RUN mkdir /etc/service/pester
ADD pester.py /etc/service/pester/run
RUN chmod u+x /etc/service/pester/run

CMD ["/sbin/my_init"]

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
