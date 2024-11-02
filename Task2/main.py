import turtle


def draw_pythagoras_tree(t, branch_length, angle, depth):
    if depth == 0:
        return

    # Малюємо основний стовбур дерева
    t.forward(branch_length)

    # Зберігаємо поточне положення та кут
    position = t.position()
    heading = t.heading()

    # Ліва гілка
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * 0.7, angle, depth - 1)

    # Повертаємося в початкове положення та кут
    t.penup()
    t.goto(position)
    t.setheading(heading)
    t.pendown()

    # Права гілка
    t.right(angle)
    draw_pythagoras_tree(t, branch_length * 0.7, angle, depth - 1)

    # Повертаємося в початкове положення та кут
    t.penup()
    t.goto(position)
    t.setheading(heading)
    t.pendown()

    # Повертаємо черепашку у вихідне положення
    t.backward(branch_length)


def main():
    # Налаштування екрану
    screen = turtle.Screen()
    screen.title("Фрактал 'Дерево Піфагора'")
    screen.bgcolor("white")

    # Створення черепашки
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.left(90)  # Повертаємо черепашку вгору
    t.color("brown")  # Колір дерева

    # Початкові параметри
    branch_length = 100  # Довжина першої гілки
    angle = 30  # Кут розгалуження
    depth = int(input("Введіть рівень рекурсії для фрактала 'дерево Піфагора': "))

    # Малювання дерева
    draw_pythagoras_tree(t, branch_length, angle, depth)

    # Завершення
    turtle.done()


if __name__ == "__main__":
    main()