# Набор различных утилит для отладки приемника AIS и не только

## Постановка задачи 
1. Записать [AIS](https://xakep.ru/2024/09/12/decoding-ais/) сигнал с приемника в [IQ файл](https://www.radioscanner.ru/info/article378/) для последующего изучения и декодирования
2. Создать простой декодер AIS сигнала в GNU Radio (далее, [GRC](https://www.gnuradio.org/)) на базе стандартных компонент (блоков)
3. Отладить декодирование AIS и его преобразование в сообщения [NMEA 0183](https://orsyst.ru/blog/nmea)

## Окружение 
### Софт
* Операционная система Ubuntu Ubuntu 24.04.3 LTS
* Visual Studio Code v1.108.2
* GNU Radio v3.10.9.2 (Python 3.12.3)
### Железо
* Приемник [Малахит DSP3](https://malahiteam.com/product/priemnik-malahit-dsp3/) с прошивкой [FW 2.40](https://drive.google.com/drive/u/0/folders/1JDsT4t-Jco0wV7BmWuLnzKwpz76EqyX4)

## Смотреть детали
1. [Запись IQ сигнала](rec/README.md) с помощью приемника [Малахит DSP3](https://malahiteam.com/product/priemnik-malahit-dsp3/)
2. [Извлечение AIS пакета](demod/README.md) в [GRC](https://www.gnuradio.org/) на базе стандартных компонент (блоков)
3. [Эксперименты с радиомодулями](rf/README.md) для приемника AIS

## Полезные ссылки
1. [Перехватываем и разбираем сигнал AIS](https://xakep.ru/2024/09/12/decoding-ais/)
2. [В помощь радиолюбителю: принимаем сигналы AIS морских судов](https://habr.com/ru/companies/ru_mts/articles/820177/). Описаны пайплайны для Windows и Linux для приема и декодирования AIS сигналов судов с отображением на карте
3. [SDR — как это работает? Часть 1](https://habr.com/ru/articles/451674/)
4. [SDR — как это работает? Часть 2](https://habr.com/ru/articles/452036/)
5. [SDR — как это работает? Часть 3](https://habr.com/ru/articles/452390/)
6. [SDR — как это работает? Часть 4](https://habr.com/ru/articles/452390/)
7. [SDR — как это работает? Часть 5](https://habr.com/ru/articles/453454/)
8. [SDR — как это работает? Часть 6](https://habr.com/ru/articles/453766/)

