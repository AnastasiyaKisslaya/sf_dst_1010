"""Игра угадай число
компьютер сам загадывает и сам угадывает число
"""
    
import numpy as np
    
def random_predict(number:int = np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
        
    count = 0
    max_number = 100
    min_number = 0
    predict_number = np.random.randint(1, 101) # предполагаемое число 
      
    while True:
        count += 1
        
        if predict_number > number:
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2
        elif predict_number < number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2
        else:        
            break #выход из цикла, если угадали
    return count

def score_game(random_predict) -> int:
    """For how manyattemps on average out of 100 approaches our algorithm guesses

    Args:
        random_predict ([type]): guess function
    Returns:
        int: average number of attemps
    """
 
    count_ls = [] # list to save the number of attemps
    random_array = np.random.randint(1, 101, size=(1000)) # made a list of numbers
    
    i = 0
    for number in random_array:
        i += 1
        
    count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # find the average number of attempts
    
    print(f'Your algorithm guesses the number in the middle for: {score} attempt')
    
    return (score)


# RUN
if __name__ == '__main__':
    score_game(random_predict)

