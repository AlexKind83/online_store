function display (selected) {
    if (selected == 'infofirstbox') {
        texttoshow = "<h5>Доставка и оплата</h5> <p>Здесь должна находится информация о доставке и оплате, но ее пока нет.</p>";
    }
    else if (selected == 'infosecondbox') {
        texttoshow = "<h5>Контактная информация</h5> <p>Здесь должен находится адрес и телефоны нашей компаний, но их пока нет.</p>";
    }
    else if (selected == 'infothreebox') {
        texttoshow = "<h5>Про нас</h5> <p>Здесь должна находится информация о, развитий нашей фирмы, но ее пока нет.</p>";
    }
    document.querySelector('#siteinfotext').innerHTML = texttoshow;
}
