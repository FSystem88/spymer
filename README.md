[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0) ![repo-size](https://img.shields.io/github/repo-size/s0563858/spymer)
![logo](https://raw.githubusercontent.com/s0563858/spymer/master/logo.jpg)
#
SMS-спамер который спамит СМС-подтверждениями с разных сайтов.<br>
Данный проэкт является форком следуйщего <a href="https://github.com/FSystem88/spymer">проекта</a>.<br>
Только для России!<br>

# Функции:
Данный спамер содержит следуйщие функции:
1. Спам СМС-подтверждениями с 16 разных сервисов
2. Возможность установить количество спам-рассылок (= сколько раз должны быть отосланы СМС-подтверждения)
3. Спам сразу на несколько номеров
4. Спам через прокси (чтобы скрыть IP и избежать блокировки при спаме)
5. Спам через один прокси или сразу через несколько
6. Асинхронность - рассылка спама производится быстрее чем у оригинала (= программа пытается отослать смс сразу через несколько сервисов и не ждет пока отсылка через один сервис будет успешной)
7. Функция автоматической смены прокси после каждой спам рассылки
8. Возможность просто добавлять новые сервисы (в файле <code>servicesList.py</code>)

# Как установить?
Просто следуйте следуйщей инструкции<br>
## Android:
Если у вас Android - скачать <a href="https://play.google.com/store/apps/details?id=com.termux&hl=ru">Termux из Google Play</a>, открыть его и прописать команды ниже:<br>
     <code>apt update</code><br>
     <code>apt upgrade</code><br>
     <code>apt install git</code><br>
     <code>git clone https://github.com/s0563858/spymer</code><br>
     <code>cd spymer</code><br>
     <code>python3 setup.py install</code><br>
     <code>tspam</code><br>

## iOS:
Если у вас iOS - скачать <a href="https://apps.apple.com/ru/app/testflight/id899247664">Testflight из App Store</a>, после чего присоедениться к тестированию <a href="https://testflight.apple.com/join/97i7KM8O">iSH в Testflight</a> и прописать команды ниже:<br>
     <code>apk update</code><br>
     <code>apk upgrade</code><br>
     <code>apk add git</code><br>
     <code>git clone https://github.com/s0563858/spymer</code><br>
      <code>cd spymer</code><br>
     <code>python3 setup.py install</code><br>
     <code>tspam</code><br>
    <br>
## Linux/MacOS:
Установка на Linux и MacOS аналогична установке на Android, только без Termux'a, достаточно прав SU и терминала.<br>


## Windows:
С начала установите Windows WSL - как это делается можно посмотреть <a href="https://www.youtube.com/watch?v=HYuFw-YldjU">здесь</a>.
После установки Ubuntu WSL - запустите Ubuntu WSL и пробейте следуйщие комманды:<br>
    <code>sudo add-apt-repository universe</code><br>
    <code>sudo apt-get update</code><br>
    <code>sudo apt install git</code><br>
    <code>git clone https://github.com/s0563858/spymer</code><br>
     <code>cd spymer</code><br>
     <code>python3 setup.py install</code><br>
     <code>tspam</code><br>



# LICENSE
**Лицензия: MPL-2.0**<br>
Глаголит она о том, что если у вас будут хоть какие то проблемы с законом, то <b>эти проблемы остаются вашими</b>, ибо я всего лишь программист, а вы использовали мою программу в своих корыстных целях!
