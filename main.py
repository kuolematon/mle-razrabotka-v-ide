import pandas as pd

from src.reporter import DataFrameReporter


def main():
    # Загружаем данные
    data = pd.read_csv('data/payments.csv')

    # Создаём объекты с разными настройками
    reporter_1 = DataFrameReporter(
        float_format='0.02f',
        percent_format='0.03%'
    )

    reporter_2 = DataFrameReporter(
        float_format='0.03f',
        percent_format='0.01%',
        include_all=True
    )

    # Выводим первый отчёт
    reporter_1.show_report(data, 'Отчёт в формате 1:')

    print()

    # Выводим второй отчёт
    reporter_2.show_report(data, 'Отчёт в формате 2:')


if __name__ == '__main__':
    main()
