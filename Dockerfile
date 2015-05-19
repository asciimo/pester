RUN echo 'Beginning pester...'
FROM phusion/baseimage:0.9.16

RUN pip install requests
RUN mkdir /etc/service/pester
ADD pester.py /etc/service/pester/run

CMD ["/sbin/my_init"]

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
