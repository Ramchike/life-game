![логотип](https://imgbly.com/ib/TrkqgixW94.png)

## Описание проекта
Проект представляет собой реализацию игры "Жизнь" с использованием библиотеки Pygame на языке Python. Игра "Жизнь" представляет собой клеточный автомат, в котором каждая клетка на игровом поле может находиться в одном из двух состояний: "живое" или "мертвое". Игра эволюционирует в соответствии с простыми правилами, определяющими, какие клетки остаются живыми, а какие умирают.

## Основной функционал
1. **Отображение игрового поля**: Пользователь видит игровое поле, на котором отображаются клетки.
2. **Изменение состояния клеток**: Пользователь может изменять состояние клеток (живые/мертвые) с помощью мыши.
3. **Старт и окончание игры**: Пользователь может начать игру, а также игра завершается, когда все клетки умирают или проходит определенное количество времени.

## Ключевые компоненты
- **Button**: Класс, представляющий кнопку в пользовательском интерфейсе. Он отображает кнопку на экране и обрабатывает события нажатия на нее.
- **Board**: Класс, представляющий игровое поле. Он отвечает за отрисовку клеток, обработку нажатий на клетки и выполнение логики игры.
- **MainMenu**: Класс, отображающий главное меню игры и обрабатывающий события взаимодействия с кнопками меню.
- **GamePage**: Класс, представляющий игровую страницу. Он отображает игровое поле и кнопки для управления игрой, а также содержит логику обновления игрового поля и проверки условий окончания игры.
- **Game**: Класс, отвечающий за запуск игры. Он создает экземпляр главного меню и запускает основной игровой цикл.

## Зависимости
- Python 3.x
- Pygame

## Запуск проекта
1. Установите Python, если он не установлен.
2. Установите библиотеку Pygame с помощью pip.

# Входные данные / Действия:
### Главное меню:
1. **Начать игру**: Нажмите на кнопку "Начать игру", чтобы перейти к игровой странице и начать игру.
2. **Настройки**: Пока не реализовано.
3. **Выйти**: Нажмите на кнопку "Выйти", чтобы закрыть игру.
### Игровая страница:
1. **Старт**: Нажмите на кнопку "Старт", чтобы начать игру. После этого начнется эволюция клеток на игровом поле в соответствии с правилами игры "Жизнь".
2. **Назад (<)**: Нажмите на кнопку "Назад", чтобы выйти из игры.
### Игровое поле:
1. **Клик мышью**: Чтобы изменить состояние клетки (живая/мертвая), кликните на нее левой кнопкой мыши. Это может повлиять на дальнейшую эволюцию клеток на поле.

Пользователь может взаимодействовать с игрой, нажимая на соответствующие кнопки и изменяя состояние клеток на игровом поле. Вся игровая логика зависит от действий пользователя и правил игры "Жизнь".
