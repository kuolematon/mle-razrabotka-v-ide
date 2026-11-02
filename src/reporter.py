class DataFrameReporter:
    def __init__(self, float_format='0.05f',
                 percent_format='0.02%', include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, df, title=None):
        if title:
            print(title)

        print('Количество столбцов:', df.shape[1])
        print('Количество строк:', df.shape[0])

        duplicates = df.duplicated().sum()
        print('Количество дубликатов:', duplicates)

        duplicate_share = duplicates / df.shape[0] if df.shape[0] else 0
        print('Доля дубликатов:', format(duplicate_share, self.percent_format))

        print(df.describe(include='all' if self.include_all else None))

        missing_count = df.isna().sum().sum()
        missing_share = missing_count / df.size if df.size else 0

        print('Количество пропусков:', missing_count)
        print('Доля пропусков:', format(missing_share, self.float_format))