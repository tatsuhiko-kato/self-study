def after_greeting(func, name):
    func(name)
    print('今日はいいお天気ですね')

def greeting(name):
    print(f'こんにちは。{name}さん')

after_greeting(greeting, 'john')