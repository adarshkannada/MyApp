import matplotlib as mp
from src.main.data.fetch_data import FetchData
from loguru import logger


class DataPlots:
    def define_bar_chart(self):
        df = FetchData().load_data(rows=32, worksheet='jul 2023', header_col_num=1)

        # logger.info(df)
        ndf = df.iloc[31].tolist()
        ndf_final = ndf[1:]
        print(ndf_final)
        # n_list = ndf['Jul23'].tolist()
        # print(n_list)


DataPlots().define_bar_chart()
