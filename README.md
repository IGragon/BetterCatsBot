# BetterCatsBot

## Описание
Бот построен на асинхронной библиотеке aiogram и задеплоен на heroku
Используется webhook

## Функции бота
/start - выводит приветствие

/cat - переходит в режим обработки изображений

/help - выходит из любого режима и отправляет список команд с описанием

## Обработка изображений
Изображения улучшаются SRRes-Net обученой на датасете с кошками 150 эпох

Из-за ограничения heroku на 500 Мб памяти изображения более 200px в любой размерности будут ужиматься до 200px в этой размерности.
