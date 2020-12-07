# Космический Инстаграм
Небольшой набор скриптов для скачивания фотографий из api [spacex](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1) и [hubble](http://hubblesite.org/api/documentation), а также их публикации в [instagram](https://www.instagram.com/).
## Как установить
* Склонируйте репозиторий
* Установите зависимости
```bash
pip install -r requirements.txt
```
* Создайте в проекте файл `.env`
* Заполните `.env` следующими переменными:
  
  `INSTAGRAM_USER_NAME` - Логин вашего аккаунта 
  
  `INSTAGRAM_USER_NAME` - Пароль вашего аккаунта

### Как пользоваться
Вы можете скачать фотографии [spacex](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1)
```bash
python fetch_spacex.py
```
или [hubble](http://hubblesite.org/api/documentation)
```bash
python fetch_hubble.py
```
Для того, чтобы опубликовать фотографии в [instagram](https://www.instagram.com/)
```bash
python publication_photo_to_instagram.py
```
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/modules/).
