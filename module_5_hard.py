# DeBach
# Module_5_hard"Свой YouTube"


import time

# _____________________________________________________________________________________________
class User:

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname  # имя пользователя, строка
        self.password = password  # пароль, число
        self.age = age # возраст, число

    def __str__(self):
        return self.nickname


# _____________________________________________________________________________________________
class Video:

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title  # заголовок, строка
        self.duration = duration  # продолжительность, секунды
        self.time_now = 0  # секунда остановки (изначально 0)
        self.adult_mode = adult_mode  # ограничение по возрасту, bool (False по умолчанию)

    def __eq__(self, other): # сравнение заголовков
        return self.title == other.title


    def __contains__(self, item):
        return item in self.title


# _____________________________________________________________________________________________
class UrTube:

    users = []
    videos = []
    current_user = None

    def log_in(self, nickname: str, password: int):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
                return

    def register(self, nickname: str, password: int, age: int):
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")


        user = User(nickname, password, age)
        self.users.append(user)
        self.log_out()
        self.log_in(user.nickname, user.password)

    def log_out(self):  # сброс текущего пользователя
        self.current_user = None

    def add(self, *args):
        for one_video in args:
            if one_video.title not in [video_in_videos.title for video_in_videos in self.videos]:
                self.videos.append(one_video)

    def get_videos(self, text: str):
        list_title_text = []
        for one_video in self.videos:
            if text.lower() in one_video.title.lower():
                list_title_text.append(one_video.title)
        return list_title_text

    def watch_video(self, text_user):
        if self.current_user:
            for one_video in self.videos:
                if text_user in one_video.title:
                    if one_video.adult_mode is True:
                        if self.current_user.age < 18:
                            print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        else:
                            for i in range(1, 11):
                                print(i, end=' ')
                                time.sleep(1)
                                one_video.time_now += 1
                            one_video.time_now = 0
                            print('Конец видео')

                    else:
                        for i in range(1, 11):
                            print(i, end=' ')
                            time.sleep(1)
                            one_video.time_now += 1
                        one_video.time_now = 0
                        print('Конец видео')

        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


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
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
