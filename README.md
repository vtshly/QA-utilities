# QA-utilities

*There are my developments for useful utilities in software testing.*

> **The idea is simple - we need tools for filling out forms and generating data.**

For testing web applications we have extensions like [Bug magnet](https://github.com/gojko/bugmagnet) or [Fake Data](https://www.fakedata.pro/)

But what if we fill in the data **outside the web browser**? In Desktop applications, or databases, or anywhere else...

I decided to reinvent the bicycle and write some scripts *to get data generator wherever I want*.

For scripting i used Python and for calling these sripts i use text-expander [Espanso](https://github.com/espanso/espanso) because of FOSS and multiplatform.

## String Generator

* Put `string-generator.yml` file in espanso directory (or use [imports](https://espanso.org/docs/matches/organizing-matches/#imports)) and `string-generator.py` file in `../scripts` folder
* Then, just type abbreviation `:genstr` and write numbers of string length into input form


![gif](./media/string-generator.gif)


## Multiple fields filling out

* comming soon

## Fake Data Generation

* Put file `fake-data-gen.yml` in espanso directory (oe user imports). 
* Put files `fake-*.py` in `../scripts` folder
* Press `ALT`+`SPACE` for espanso search box.
* Find fake generator. Press `ENTER`

![fake-data-gen.gif](./media/fake-data.gif)
