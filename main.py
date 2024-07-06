from colorama import init

init()
from colorama import Fore, Style


class User:
    """
    Класс пользователя. Содержит Login (nickname), hash password, age - возраст
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    """
    Клас Видео содержит
    title(заголовок),
    duration(продолжительность видео),
    time_now(секунда остановки),
    adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        """
        Вывод информации о видео
        :return: строка для печати
        """
        list_ = list(map(lambda x, y: '\n\t' + str(x) + ' = ' + str(y), self.__dict__.keys(),
                         self.__dict__.values()))
        return f' '.join(list_)
class UrTube:
    """
    Класс Urtube
    Содержит список пользователей, список видео, текущего пользователя
    и различне методы работы с ними
    """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __contains__(self, user=None, video=None, password=None):
        """
        Метод проверяет существует ли пользователь или видео в базе
        :param user: пользователь для проверки
        :param video: видео для проверки
        :return: номер позиции +1, либо 0, в случае, если ничего не найдено
        """
        if user == None:
            if video == None:
                return False
            else:
                for i in range(len(self.videos)):
                    if str(self.videos[i].title).upper() == video.upper():
                        return i + 1
                return 0
        else:
            for i in range(len(self.users)):
                if str(self.users[i]) == user:
                    if password is None:
                        return i + 1
                    if self.users[i].password == password:
                        return i + 1
                    else:
                        return 0
            return 0
    def __str__(self):
        """
        Вывод информации об объекте.
        1. Список пользователей
        2. Список видео
        :return: Строку с текущим пользователем, т.к. весь вывод осуществляется внутри метода
        """
        print(Fore.YELLOW + Style.BRIGHT + '\nСписок пользователей:\n' + Style.RESET_ALL)
        for i in self.users:
            print(Fore.YELLOW, '\t' + str(i), Style.RESET_ALL)

        print(Fore.CYAN + Style.BRIGHT + '\nСписок видео:' + Style.RESET_ALL)
        for i in self.videos:
            print(Fore.CYAN, i, Style.RESET_ALL)

        return Fore.LIGHTBLUE_EX + f'\nТекущий пользователь {self.current_user}\n' + Style.RESET_ALL

    def register(self, nickname, password, password_confirm, age):
        """
        Регистрация пользователя в системе
        :param nickname: Имя пользователя
        :param password: Пароль
        :param password_confirm: Повторный ввод пароля
        :param age: Возраст
        :return: Ничего не возвращает
        """
        if nickname not in self:
            if password == password_confirm:
                self.users += [User(nickname, password, age)]
                self.log_in(nickname, password)
            else:
                print(Fore.RED, '\nПароли не совпадают. Попробуйте еще раз.',
                      Style.RESET_ALL)
        else:
            print(Fore.RED + f'\nПользователь {nickname} уже существует',
                  Style.RESET_ALL)

    def log_in(self, nickname, password):
        """
        Вход пользователя в систему
        :param nickname: Имя пользователя
        :param password: hash пароля
        """

        bool_ = self.__contains__(nickname, password=password)
        if bool_:
            print(Fore.LIGHTBLUE_EX, f'\nПользователь {nickname} вошел в систему', Style.RESET_ALL)
            self.current_user = self.users[bool_ - 1]
        else:
            print(Fore.RED, '\nТакого пользователя нет в базе. Вход не был выполнен.', Style.RESET_ALL)

    def log_out(self):
        """
        Выход из системы
        :return: Ничего не возвращает
        """
        self.current_user = None
    def add(self, *video):
        """
        Метод добавляет видео
        :param video: список объектов класса Video
        :return: Ничего не возвращает
        """
        for vid_ in video:
            if self.__contains__(video=vid_.title):
                print(
                    Fore.RED + f'Видео {vid_.title} уже существует в базе.' + Style.RESET_ALL)
            else:
                self.videos += [vid_]

    def get_videos(self, video):
        """
        Метод get_videos принимает поисковое слово и возвращает список названий
        всех видео, содержащих поисковое слово. Поиск осуществляется без учета регистра.
        :param video: Слово для поиска
        :return: Список названий всех видео
        """
        res = []
        for i in self.videos:
            if video.upper() in str(i.title).upper():
                res += [i.title]
        return res

    def watch_video(self, video):
        """
        Метод watch_video, который принимает название фильма, если не находит точного совпадения
        (вплоть до пробела), то ничего не воспроизводится, если же находит ведётся отчёт в консоль
        на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
        :param video: Название видео
        :return: Ничего не возвращает
        """
        from time import sleep, time_ns

        def time_out(sec_=1):
            """
            Ожидает нажатия клавиши для прерывания таймаута
            Плохо работает в консоли
            :param sec_: таймаут
            :return: нажатую клавишу
            """
            from msvcrt import kbhit, getch

            start_time = time_ns()
            inp = None

            while True:
                if kbhit():
                    inp = getch()
                    break
                elif time_ns() - start_time > sec_ * 10 ** 9:
                    break

            if inp:
                return inp
            else:
                return None

        if ur.current_user == None:
            print(Fore.RED + '\nВойдите в аккаунт чтобы смотреть видео' + Style.RESET_ALL)
            return

        bool_ = self.__contains__(video=video)
        if bool_:
            if self.videos[bool_ - 1].adult_mode and self.current_user.age < 18:
                print(Fore.RED + '\nВам нет 18 лет, пожалуйста покиньте страницу' + Style.RESET_ALL)
                return
        else:
            print(Fore.RED + f'\nТакого видео "{Style.BRIGHT + video + Style.NORMAL}" нет в базе' + Style.RESET_ALL)
            return

        print(Fore.CYAN + f'\nПросмотр видео "{Style.BRIGHT + video + Style.NORMAL}" начался:')
        for i in range(self.videos[bool_ - 1].time_now, self.videos[bool_ - 1].duration + 1):
            print(i, end=' ')
            # sleep(1)
            if time_out() != None:
                print('Воспроизведение прервано ' + Style.RESET_ALL)
                self.videos[bool_ - 1].time_now = i
                return
        print('Конец видео' + Style.RESET_ALL)
        self.videos[bool_ - 1].time_now = 0
if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', hash('lolkekcheburek'), hash('lolkekcheburek'), 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', hash('iScX4vIJClb9YQavjAgF'), hash('iScX4vIJClb9YQavjAgF'), 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', hash('F8098FM8fjm9jmi'), hash('F8098FM8fjm9jmi'), 55)

    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

    # ============================================================================
    # Далее не для проверки, а для тренировки
    # Попытка входа с неправильным паролем и вход с правильным паролем
    ur.log_in('vasya_pupkin', hash('F8098FM8fjm9jmi'))
    ur.log_in('vasya_pupkin', hash('lolkekcheburek'))

    print(ur)

    # Ввод пользователем данных, поиск и просмотр видео в цикле

    choice_dic = {
        0: 'Завершить работу,',
        1: 'Регистрация пользователя,',
        2: 'Вход в систему UrTube,',
        3: 'Выход из ситемы,',
        4: 'Добавить видео,',
        5: 'Поиск видео по ключевому слову,',
        6: 'Просмотр видео,',
        7: 'Вывести содержимое всей базы.',
        8: 'Вывести список видео в базе'
    }
    choice_ = 1
    while choice_:
        choice_ = input('\nВыберете одно из следующих действий:\n' +
                        ''.join(list(map(lambda x, y: '\t' + str(x) + ' = ' + str(y) + '\n', choice_dic.keys(),
                                         choice_dic.values()))))
        choice_ = int(choice_) if choice_.isnumeric() else 10
        if choice_ == 0:
            exit()
        if choice_ == 1:
            ur.register(input('Введите имя пользователя для регистрации: '), hash(input('Введите пароль: ')),
                        hash(input('Повторите пароль: ')), int(input('Введите возраст: ')))
        elif choice_ == 2:
            ur.log_in(input('\nВведите имя пользователя для входа: '), hash(input('Введите пароль: ')))
        elif choice_ == 3:
            ur.log_out()
        elif choice_ == 4:
            ur.add(Video(input('Введите Название видео: '), int(input('Введите продолжительность видео в секундах: ')),
                         adult_mode=bool(input('Введите возрастные ограничения 18+: '))))
        elif choice_ == 5:
            print(Fore.LIGHTCYAN_EX + 'Список найденных видео: ' +
                  str(ur.get_videos(input('Введите строку для поиска видео: '))) + Style.RESET_ALL)
        elif choice_ == 6:
            ur.watch_video(input('Введите название видео для просмотра полностью: '))
        elif choice_ == 7:
            print(ur.v1)
        else:
            print(ur)