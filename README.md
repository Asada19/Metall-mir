# mars-group.pro



## Начало устрановки

## Требования

Для запуска этого проекта вам потребуется установить следующее:
- Docker: [Ссылка на установку Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Ссылка на установку Docker Compose](https://docs.docker.com/compose/install/)

## Запуск проекта

1. Склонируйте репозиторий:

```bash
git clone https://github.com/Asada19/Metall-mir.git
cd web_mark 
```

2. Добавьте зависимости в .env

```bash
touch .env
cp env.example .env
```


3. Запустите docker-compose:

```bash
docker-compose up --build
```
___

### Endpoints:
```djangourlpath
GET   api/v1/catalog/  #cписок категорий 
GET   api/v1/catalog/<int:pk>  #детализация категории со вложенными услугами 
GET   api/v1/item/ #список товаров 
GET   api/v1/item/<int:pk>/   #детализация товара 
POST  api/v1/callbacks/  #обратная связь
GET   api/v1/ contacts/ #контакты (которые рядом с заявкой)
GET   api/v1/ social-media/ #социальные сети
```

___
### *Stack:*
- `python: 3.9`
- `djangoDjango:4.2.4`
- `djangorestframework:3.14.0`