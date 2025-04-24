# Устанавливаем базовый образ с Node.js
FROM node:18

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем все остальные файлы проекта
COPY . .

# Строим проект для продакшн окружения
RUN npm run build

# Устанавливаем nginx для сервировки собранного проекта
FROM nginx:alpine

# Копируем файлы из build в папку, доступную для nginx
COPY --from=0 /app/dist /usr/share/nginx/html

# Открываем порт 80 для nginx
EXPOSE 80

# Запускаем nginx
CMD ["nginx", "-g", "daemon off;"]
