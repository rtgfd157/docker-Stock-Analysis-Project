FROM ubuntu 
ENV PYTHONUNBUFFERED 1
RUN mkdir /App
RUN  apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN  yes | apt-get install python
RUN  yes | apt-get install nodejs
RUN  yes | apt-get install python3-dev default-libmysqlclient-dev build-essential
RUN  yes |apt-get install python3-pip
RUN  yes | apt-get install npm

# https://stackoverflow.com/questions/30716937/dockerfile-build-possible-to-ignore-error
RUN  npm i -g @vue/cli  2>&1 > install_docker.log || echo "There were failing in npm i -g @vue/cli  !"
# RUN npm i -g @vue/cli


WORKDIR /App
COPY requirements.txt /App/
RUN pip3 install -r requirements.txt
COPY App /App/


WORKDIR App/stock_analysis_project

# FROM  node as frontend
# RUN mkdir /frontend
# WORKDIR /frontend
# RUN  yes | apt-get install npm
# RUN npm i -g @vue/cli
# COPY App/stock_analysis_project/frontend /frontend/


#RUN python manage.py makemigrations
#RUN  yes |  python manage.py migrate 

#RUN yes | python manage.py collectstatic