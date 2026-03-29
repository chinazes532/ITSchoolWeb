<h1 align="center">💻 ITSchoolWeb</h1>

<p align="center">
  Фулл-стек проект для частной IT-школы<br>
  <b>Курсовая работа:</b> «Проектирование и реализация web-интерфейса сайта учебного учреждения»
</p>

<hr>

<h2>📌 Описание проекта</h2>

<p>
ITSchoolWeb — это веб-приложение для частной школы программирования.
Пользователи могут просматривать информацию о школе и оставлять заявку на консультацию.
</p>

<ul>
  <li>📢 Новости и мероприятия</li>
  <li>📅 Расписание занятий</li>
  <li>💰 Стоимость обучения</li>
  <li>📊 Ведомость</li>
  <li>📝 Форма записи на консультацию</li>
</ul>

<p>
После отправки формы данные:
</p>

<ul>
  <li>сохраняются в базе данных</li>
  <li>отправляются на почту администрации 📩</li>
</ul>

<hr>

<h2>🛠️ Стек технологий</h2>

<p>
<b>Backend:</b> Python, FastAPI, SQLAlchemy<br>
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
  <li>Отправка email-уведомлений администратору</li>
</ul>

<hr>

<h2>📁 Структура проекта</h2>

<pre>
ITSchoolWeb/
│
├── backend/          # Серверная часть (FastAPI)
├── frontend/         # Клиентская часть (React)
├── docker-compose.yml
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
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

GMAIL_SENDER=
GMAIL_PASSWORD=
ADMIN_MAIL=
</pre>

<h3>3. Запуск проекта</h3>

<pre>
docker compose up -d --build
</pre>

<hr>

<h2>🌐 Использование</h2>

<ul>
  <li>Фронтенд: <b>http://ВАШ_IP:3000</b></li>
  <li>Backend API: <b>http://ВАШ_IP:8000/docs</b></li>
</ul>

<hr>

<h2>🧠 Архитектура проекта</h2>

<ul>
  <li>Используется <b>SQLAlchemy</b> для работы с БД</li>
  <li>Реализован паттерн <b>Repository + Service</b></li>
  <li>Разделение логики:
    <ul>
      <li>Repository — работа с базой данных</li>
      <li>Service — бизнес-логика</li>
    </ul>
  </li>
  <li>Email сервис реализован через <b>smtplib</b></li>
</ul>

<hr>

<h2>📬 Почтовая система</h2>

<p>
При отправке заявки:
</p>

<ul>
  <li>данные сохраняются в PostgreSQL</li>
  <li>на почту администратора приходит уведомление</li>
</ul>

<hr>

<h2 align="center">🚀 Проект готов к расширению и доработке</h2>
