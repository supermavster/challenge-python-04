# -*- codign: utf-8 -*-

def div(func):
    # You have to code here!
    def wrapper(*args, **kwargs):
        element, data = 'div', func(*args)
        print(f'<{element}>{data}</{element}>')
        return data
    return wrapper


def article(func):
    # You have to code here!
    def wrapper(*args, **kwargs):
        element, data = 'article', func(*args)
        print(f'<{element}>{data}</{element}>')
        return data
    return wrapper


def p(func):
    # You have to code here!
    def wrapper(*args, **kwargs):
        element, data = 'p', func(*args)
        print(f'<{element}>{data}</{element}>')
        return data
    return wrapper


# Here you must apply the decorators, uncomment this later
@div
@article
@p
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
