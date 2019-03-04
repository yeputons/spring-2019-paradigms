print('import lib_b')
import lib_b  # Требует lib_a и загружает его
print('import lib_с')
import lib_c  # Тоже требует lib_a, но второй раз не загружается
print('end')
