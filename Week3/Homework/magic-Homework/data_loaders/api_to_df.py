import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    df_total = pd.DataFrame()

    for i in range(12):
        url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{i+1:02}.parquet'
        print(url)
        df = pd.read_parquet(url)
        df_total = pd.concat([df_total,df])

    return df_total


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
