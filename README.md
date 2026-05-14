<h1 align="center">💻 ITSchoolWeb</h1>

<p align="center">
  Фулл-стек проект для частной IT-школы<br>
  <b>Курсовая работа:</b> «Проектирование и реализация web-интерфейса сайта учебного учреждения»
</p>

<hr>

<h2>📌 Описание проекта</h2>

<p>
ITSchoolWeb — это современное веб-приложение для частной школы программирования. 
Система оптимизирована для быстрой работы пользователя: тяжелые операции (отправка email) вынесены в фоновые задачи.
</p>

<ul>
  <li>📢 Новости и мероприятия</li>
  <li>📅 Расписание занятий</li>
  <li>💰 Стоимость обучения</li>
  <li>📊 Ведомость</li>
  <li>📝 Форма записи на консультацию</li>
</ul>

<p>
<b>Процесс обработки заявки:</b>
</p>

<ul>
  <li>Данные мгновенно сохраняются в PostgreSQL</li>
  <li>Задача на отправку Email передается в <b>Celery</b> через брокер <b>Redis</b></li>
  <li>Пользователь получает ответ за миллисекунды, пока уведомление отправляется в фоне 🚀</li>
</ul>

<hr>

<h2>🛠️ Стек технологий</h2>

<p>
<b>Backend:</b> Python, FastAPI, SQLAlchemy, smtplib, Celery + Redis<br>
<b>Frontend:</b> React, HTML, CSS, JavaScript<br>
<b>DevOps:</b> Docker, Docker Compose<br>
<b>База данных:</b> PostgreSQL<br>
<b>Прочее:</b> Axios, Git
</p>

<hr>

<h2>⚙️ Основные возможности</h2>

<ul>
  <li>Отображение информации о школе</li>
  <li>Навигация по страницам (React Router)</li>
  <li>Отправка заявок через форму</li>
  <li>Сохранение данных в БД</li>
  <li><b>Фоновая отправка email-уведомлений</b> администратору через Celery</li>
</ul>

<hr>

<h2>📁 Структура проекта</h2>

<pre>
ITSchoolWeb/
│
├── backend/          # Серверная часть (FastAPI, Celery Workers)
├── frontend/         # Клиентская часть (React)
├── docker-compose.yml # Оркестрация (App, DB, Redis, Celery, Backend, Frontend)
└── README.md
</pre>

<hr>

<h2>🚀 Быстрый старт</h2>

<h3>1. Клонирование проекта</h3>

<pre>
git clone https://github.com/chinazes532/kursach.git
</pre>

<h3>2. Настройка окружения</h3>

<p>Создайте файл <b>.env</b> в папке <b>backend</b>:</p>

<pre>
# База данных
POSTGRES_DB=kursach_work
POSTGRES_USER=
POSTGRES_PASSWORD=

# Настройки подключения к БД
DB_HOST=db
DB_PORT=5432

# Redis
REDIS_URL

# Email (SMTP)
GMAIL_SENDER=
GMAIL_PASSWORD=
ADMIN_MAIL=

# URL фронтенда
FRONTEND_URL=
</pre>

<p>Создайте файл <b>.env</b> в папке <b>frontend</b>:</p>

<pre>
REACT_APP_BASE_URL=
</pre>

<h3>3. Запуск проекта</h3>

<pre>
docker compose up -d --build
</pre>

<hr>

<h2>🌐 Использование</h2>

<ul>
  <li>Фронтенд: <b>http://ВАШ_IP:3000</b></li>
  <li>Backend API (Swagger): <b>http://ВАШ_IP:8000/docs</b></li>
  <li>Redis: <b>port 6379</b></li>
  <li>SMTP: <b>port 465</b></li>
</ul>

<hr>

<h2>🧠 Архитектура проекта</h2>

<ul>
  <li>Используется <b>SQLAlchemy</b> для работы с БД</li>
  <li>Реализован паттерн <b>Repository + Service</b></li>
  <li><b>Background Tasks:</b> Использование Celery позволило сократить время ответа сервера на ~2-4 секунды (время ожидания ответа от SMTP-сервера).</li>
  <li>Разделение логики:
    <ul>
      <li>Repository — работа с базой данных</li>
      <li>Service — бизнес-логика</li>
      <li>Tasks — асинхронные задачи (Celery)</li>
    </ul>
  </li>
</ul>

<hr>

<h2 align="center">🚀 Проект оптимизирован и готов к нагрузкам</h2>
