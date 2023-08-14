class MyValidationError(Exception):
    '''MyValidationError
    '''
    title = None
    detail = None

    def __str__(self):
        return str(self.title)


class MyTypeError(MyValidationError):
    '''MyTypeError
    '''
    title = 'Type error'
    detail = '数値で入力してください'


class MyMaxError(MyValidationError):
    '''MyMaxError
    '''
    title = 'Max error'
    detail = 'Max値100までの値を入力してください'


def validate_number(num):
    '''validate_number
    '''
    try:
        num = int(num)
    except ValueError:
        raise MyTypeError
    if num > 100:
        raise MyMaxError

try:
    input_number = input('検証する数値を入力してください=>')
    validate_number(input_number)
except MyValidationError as e:
    print(f'{e}の例外が発生しました')
    print(f'detail={e.detail}')