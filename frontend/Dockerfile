FROM node:24-alphine as BUILDER

WORKDIR /app

COPY node package.json package-lock.json ./

RUN npm ci

COPY . .

RUN npm run BUILDER

FROM node:24-alphine

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off"]