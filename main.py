class BallMovement:
    def __init__(self, x_0=1.0, y_0=1.0, vx_0=1.0, vy_0=1.0, m=1.0):
        self.x_0 = x_0
        self.y_0 = y_0

        self.vx_0 = vx_0
        self.vy_0 = vy_0

        self.m = m
        self._movement = []

    def input(self):
        print("Input:")
        while True:
            try:
                self.x_0 = float(input("\tx_0 = "))
                self.y_0 = float(input("\ty_0 = "))

                self.vx_0 = float(input("\tvx_0 = "))
                self.vy_0 = float(input("\tvy_0 = "))
            except ValueError:
                print("Введенное значение не является числом. Попробуйте еще раз!")
            else:
                print('Success!')
                break

    def f_x(self, x_i, vx_i, t_i):
        return self.vx_0

    def f_y(self, y_i, vy_i, t_i):
        return self.vy_0 - 9.8 * t_i

    def move(self, t_start=None, t_end=None, dt=None):
        print('Move: ')
        # устанавливаем параметры времени
        while True:
            try:
                if t_start is None:
                    t_start = float(input("\tt_start = "))
                if t_end is None:
                    t_end = float(input("\tt_end = "))
                if dt is None:
                    dt = float(input("\tdt = "))
            except ValueError:
                print("Введенное значение не является числом. Попробуйте еще раз!")
            else:
                print('Success!')
                break

        # задаем начальные значения
        t_i = t_start
        x_i, y_i = self.x_0, self.y_0
        vx_i, vy_i = self.vx_0, self.vy_0

        # схема Эйлера
        print('t_i | x_i | y_i | vx_i | vy_i')
        while t_i <= t_end:
            x_temp = x_i + dt * vx_i
            y_temp = y_i + dt * vy_i

            vx_temp = vx_i + dt / self.m * self.f_x(x_i, vx_i, t_i)
            vy_temp = vy_i + dt / self.m * self.f_y(y_i, vy_i, t_i)

            data = f"{t_i} {x_i} {y_i} {vx_i} {vy_i}"
            self._movement.append(data)
            print(data)

            # reload
            x_i, y_i = x_temp, y_temp
            vx_i, vy_i = vx_temp, vy_temp
            t_i += dt

    def write(self, filename="data.txt"):
        if self._movement is None:
            print('Нет данных для записи. Вызовите метод move!')
        else:
            with open(filename, 'w') as file:
                for data in self._movement:
                    file.write(data + "\n")
        print(f'{filename} успешно записан!')


if __name__ == '__main__':
    ball = BallMovement(x_0=0,
                        y_0=0,
                        vx_0=10,
                        vy_0=30)

    # ball.input()

    ball.move(t_start=1,
              t_end=10,
              dt=0.1)

    ball.write()
