class User:
    current_user = False

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return self.nickname == other

    def get_password(self):
        return self.password

    def get_age(self):
        return self.age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __contains__(self, item):
        return item.lower() in self.title.lower()

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other

    def set_time_now(self):
        self.time_now += 1


class UrTube:
    def __init__(self):
        self.users = []
        self.current_user = None
        self.videos = []

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user and hash(password) == user.get_password():
                self.current_user = user
                return

    def register(self, nickname, password, age):
        if nickname not in self.users:
            user = User(nickname, password, age)
            self.users.append(user)
            # self.current_user = user
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search):
        video_list = []
        for video in self.videos:
            if search in video:
                video_list.append(video)
        return video_list

    def check_age(self, video):
        if self.current_user:
            if not video.adult_mode or self.current_user.get_age() >= 18:
                return True
            else:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')
        return False

    def watch_video(self, search_title):
        from time import sleep
        for video in self.videos:
            if search_title == video and self.check_age(video):
                while video.time_now < video.duration:
                    video.set_time_now()
                    print(video.time_now, end=" ")
                    sleep(0.5)
                print('Конец видео')
                video.time_now = 0


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
