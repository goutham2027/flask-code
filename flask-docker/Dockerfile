FROM python:2.7
MAINTAINER Goutham <goutham2027@gmail.com>

ENV HOME /flask_app
RUN mkdir /flask_app
WORKDIR /flask_app
ADD requirements.txt $HOME
RUN pip install -r requirements.txt
ADD . $HOME
ENTRYPOINT ["python"]
CMD ["app.py"]
