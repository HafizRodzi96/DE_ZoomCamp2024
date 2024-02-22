if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    print("total ride with 0 passenger :",data['passenger_count'].isin([0]).sum())
    
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    data.rename(columns={'VendorID':'vendor_id'},inplace = True)
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    # data['lpep_dropoff_date'] = data['lpep_dropoff_datetime'].dt.date
    print("total ride with 0 passenger after clean :",data['passenger_count'].isin([0]).sum())
    # Specify your transformation logic here

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block..
    """
    print("check vendor_id", 'vendor_id' in output.columns)
    assert 'vendor_id' in output.columns , 'vendor_id is not present in the DataFrame'
  
@test
def test_passenger_count(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    print("passneger count :", output['passenger_count'].isin([0]).sum() )
    assert output['passenger_count'].isin([0]).sum() >= 0, 'There is passenger count = 0'
    print("check trip distance",(output['trip_distance']==0).sum())
    assert (output['trip_distance']==0).sum() == 0 ,'There is trip distance = 0'
 