import timeit

from kmp import kmp_search
from boyer_moore import boyer_moore_search
from rabin_karp import rabin_karp_search

def read_file(name): 
    with open(name, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    
    article1 = read_file("data/article1.txt")
    article2 = read_file("data/article2.txt")

    article1_existing_substrings = [
        "Два наступні кроки – це",
        "кроці потрібно обрати чергові найбільші",
        "дві монети",
        "які важко",
        "Режим доступу до ресурсу: https://tproger.ru/articles/why-learn-algorithms/"
    ]

    article2_existing_substrings = [
        "іншими розглянутими структурами даних у використанні пам’яті значною",
        "Як видно з таблиці та рисунку найкращі",
        "Метою даної роботи",
        "даних",
        "Програмна реалізація досліджених структур"
    ]
    
    non_existing_substrings = [
        "test1test1", "hello, how are you??", "noooooo", "helloWorld228", "Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium"
    ]

    algorithms = [
        {"name": "KMP", "function": kmp_search},
        {"name": "Boyer-Moore", "function": boyer_moore_search},
        {"name": "Rabin-Karp", "function": rabin_karp_search}
    ]

    for algorithm in algorithms:
        func = algorithm.get("function")

        article1_existing_t_mean = 0
        article1_non_existing_t_mean = 0
        article2_existing_t_mean = 0
        article2_non_existing_t_mean = 0

        for i in range(5):
            article1_existing_t_mean += timeit.timeit(lambda: func(article1, article1_existing_substrings[i]), number=1)
            article1_non_existing_t_mean += timeit.timeit(lambda: func(article1, non_existing_substrings[i]), number=1)

            article2_existing_t_mean += timeit.timeit(lambda: func(article2, article2_existing_substrings[i]), number=1)
            article2_non_existing_t_mean += timeit.timeit(lambda: func(article2, non_existing_substrings[i]), number=1)

        article1_existing_t_mean /= 5
        article1_non_existing_t_mean /= 5
        article2_existing_t_mean /= 5
        article2_non_existing_t_mean /= 5

        print(algorithm.get("name"))
        print(f"article1 exsiting substrings: {article1_existing_t_mean}")

        print(f"article2 exsiting substrings: {article2_existing_t_mean}")

        
        print(f"article1 non exsiting substrings: {article1_non_existing_t_mean}")
        print(f"article2 non exsiting substrings: {article2_non_existing_t_mean}")




    


if __name__ == "__main__":
    main()