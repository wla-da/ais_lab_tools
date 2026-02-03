# Набор различных утилит для отладки приемника AIS и не только

## Постановка задачи 
1. Записать [AIS](https://xakep.ru/2024/09/12/decoding-ais/) сигнал с приемника в [IQ файл](https://www.radioscanner.ru/info/article378/) для последующего изучения и декодирования
2. Создать простой декодер AIS сигнала в GNU Radio (далее, [GRC](https://www.gnuradio.org/)) на базе стандартных компонент (блоков)
3. Отладить декодирование AIS и его преобразование в сообщения [NMEA 0182](https://orsyst.ru/blog/nmea)

## Окружение 
### Софт
* Операционная система Ubuntu Ubuntu 24.04.3 LTS
* Visual Studio Code v1.108.2
* GNU Radio v3.10.9.2 (Python 3.12.3)
### Железо
* Приемник [Малахит DSP3](https://malahiteam.com/product/priemnik-malahit-dsp3/)

## [Смотреть детали](grc/README.md) 

## Полезные ссылки
1. [Перехватываем и разбираем сигнал AIS](https://xakep.ru/2024/09/12/decoding-ais/)
1. [SDR — как это работает? Часть 1](https://habr.com/ru/articles/451674/)
1. [SDR — как это работает? Часть 2](https://habr.com/ru/articles/452036/)
1. [SDR — как это работает? Часть 3](https://habr.com/ru/articles/452390/)
1. [SDR — как это работает? Часть 4](https://habr.com/ru/articles/452390/)
1. [SDR — как это работает? Часть 5](https://habr.com/ru/articles/453454/)
1. [SDR — как это работает? Часть 6](https://habr.com/ru/articles/453766/)

