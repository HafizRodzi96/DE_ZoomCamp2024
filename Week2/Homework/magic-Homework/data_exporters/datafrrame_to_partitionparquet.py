import pyarrow as pa
import pyarrow.parquet as pq
import os
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

bucket_name = 'mage-zoomcap-hafiz'
object_key = 'your_object_key'
table_name = "ny_taxi_data"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/unified-surfer-405214-0749114cafad.json"
project_id = 'unified-surfer-405214'
root_path = f'{bucket_name}/{table_name}'

print(os.environ)

@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.
    
    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    table = pa.Table.from_pandas(data)
    print("done table")
    gcs = pa.fs.GcsFileSystem()
    print("done gcs")
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )
    print("running parequest")
    # Specify your data exporting logic here


