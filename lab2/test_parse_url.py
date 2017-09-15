import pytest
import parse_url


def test_parser():

    text = 'Московский государственный университет им. М.В.Ломоносова:\
    [Электронный ресурс]. М., 1997-2012. URL: http://www.msu.ru. \
    (Дата обращения: 18.02.2012). Ссылка на web-страницу. \
    Информация для поступающих: [Электронный ресурс] // \
    Московский государственный университет им. М.В.Ломоносова. \
    М., 1997-2012. URL: http://www.msu.ru/entrance/. \
    (Дата обращения: 18.02.2012). Ссылка на on-line-журнал \
    Секретарь-референт. 2011. № 7: [Электронный ресурс]. \
    URL: http://www.profiz.ru/sr/7_2011. (Дата обращения: 18.02.2012). \
    Ссылка на on-line-статью Каменева Е.М. Формы регистрации \
    документов: // Секретарь-референт. 2011. № 7. URL: \
    http://www.profiz.ru/sr/7_2011/formy_registracii_dokov. \
    (Дата обращения: 18.02.2012). Ссылка на on-line-книгу Степанов В. \
    Интернет в профессиональной информационной деятельности: \
    [Электронный ресурс]. 2002-2006. URL: http://textbook.vadimstepanov.ru. \
    (Дата обращения: 18.02.2012). Ссылка на часть on-line-книги \
    Степанов В. Электронные документы интернет: описание и цитирование: \
    [Электронный ресурс] // Степанов В. Интернет в профессиональной \
    информационной деятельности. 2002-2006. URL: \
    http://textbook.vadimstepanov.ru/chapter7/glava7-2.html. \
    (Дата обращения: 18.02.2012). Подробнее: \
    https://www.kakprosto.ru/kak-115149-kak-oformlyat-ssylki-iz-interneta-v-spiske-literatury#ixzz4sgFXPTlQ'

    links = parse_url.URLParser.search_for_URL(text)

    assert links == ['http://www.msu.ru', 'http://www.msu.ru/entrance/',
                     'http://www.profiz.ru/sr/7_2011',
                     'http://www.profiz.ru/sr/7_2011/formy_registracii_dokov',
                     'http://textbook.vadimstepanov.ru',
                     'http://textbook.vadimstepanov.ru/chapter7/glava7-2.html',
                     'https://www.kakprosto.ru/kak-115149-kak-oformlyat-ssylki-iz-interneta-v-spiske-literatury']

test_parser()
