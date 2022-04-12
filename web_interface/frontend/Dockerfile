FROM node:latest

# set work directory
WORKDIR /usr/src/app

# copy the whole directory (from context: ./frontend) to ./usr/src/app/
COPY . /usr/src/app/

# install requirements
RUN npm install

# START APP
ENTRYPOINT [ "npm", "start" ] 

