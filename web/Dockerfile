FROM node:20-slim AS build
WORKDIR /app
COPY package.json tsconfig.json vite.config.ts postcss.config.cjs tailwind.config.cjs /app/
COPY index.html /app/index.html
COPY src /app/src
RUN npm install && npm run build
FROM node:20-slim
WORKDIR /app
COPY --from=build /app /app
ENV HOST=0.0.0.0
EXPOSE 5173
CMD ["npm","run","dev","--","--host"]
