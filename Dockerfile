FROM node:22-alpine                

LABEL maintainer="nith@abc.com"
LABEL description="To-Do WebApp" 
LABEL version="1.0.0"

ARG BUILD_VERSION=local-dev
ENV APP_BUILD_VER=$BUILD_VERSION

WORKDIR /usr/src/app

ENV NODE_ENV=development

COPY package*.json ./

RUN npm install
COPY . .
RUN npm run build
RUN chown -R node:node /usr/src/app


USER node

EXPOSE 4173                         

HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --no-verbose --tries=1 --spider http://localhost:4173/ || exit 1

ENTRYPOINT ["npm"]                  

CMD ["run", "preview", "--", "--host", "0.0.0.0"] 