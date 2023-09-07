# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Дополнительно: реализуйте ввод из командной строки

import logging
import argparse

from HW_13_exeption import LengthError

FORMAT = '{levelname} - {asctime} {msg}'

logging.basicConfig(filename='rectangle_log.log',
                    level=logging.INFO,
                    filemode='a', 
                    format=FORMAT, 
                    style='{')
logger = logging.getLogger(__name__)


class Rectangle:

    def __init__(self, length: float, width: float = None):
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def perimetr(self):
        """Получам периметр"""
        if self.width > 0 and self.length > 0:
            res = (self.length + self.width) * 2
            logger.info(f'Посчитали периметр прямоугольника со сторонами {self.length} и {self.width}, результат = {res}')
    
        if self.width <= 0:
            logger.error(f'Прямоугольника с шириной {self.width} не существует!')
            raise LengthError(self.width, 0)
        
        if self.length <= 0:
            logger.error(f'Прямоугольника с длинной {self.length} не существует!')
            raise LengthError(self.width, 0)
        
        return res
    
    def ploshad(self):
        """Получаем площадь"""
        if self.width > 0 and self.length > 0:
            res = self.length * self.width
            logger.info(f'Посчитали площадь прямоугольника со сторонами {self.length} и {self.width}, результат = {res}')


        if self.width <= 0:
            logger.error(f'Прямоугольника с шириной {self.width} не существует!')
            raise LengthError(self.width, 0)
        
        if self.length <= 0:
            logger.error(f'Прямоугольника с длинной {self.length} не существует!')  
            raise LengthError(self.width, 0)
             
        return res
    
    def __repr__(self):
        return f"Rectangle{self.width, self.length}"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='convert()')
    parser.add_argument('-len', type=float)
    parser.add_argument('-wid', type=float)
    
    args = parser.parse_args()

    r_input = Rectangle(args.len, args.wid)
    print(r_input.perimetr(), r_input.ploshad())
 
    