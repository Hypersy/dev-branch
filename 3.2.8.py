Задание: составные сообщения об ошибках
Для закрепления материала реализуйте проверку самостоятельно. 

Вам дана функция test_input_text,  которая принимает два значения: expected_result — ожидаемый результат, и actual_result — фактический результат. Обратите внимание, input использовать не нужно!

Функция должна проверить совпадение значений с помощью оператора assert и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке. 

решение:

def test_input_text(expected_result, actual_result):
    str = expected_result
    strw = actual_result
    assert abs(expected_result == actual_result), f"expected {str}, got {strw}"