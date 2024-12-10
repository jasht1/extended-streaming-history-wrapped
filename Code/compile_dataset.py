
import os
import zipfile
import pandas

def import_streaming_history(
        file_name = "my_spotify_data.zip",
        relative_path="../Datasets/"
    ):

    dataset_path = os.path.join(
        os.path.dirname(__file__), 
        relative_path, 
        file_name)

    if zipfile.is_zipfile(dataset_path):
        with zipfile.ZipFile(dataset_path, 'r') as archive:
            file_names = archive.namelist()
            streaming_files = sorted(
                [name for name in file_names if "Streaming_History_Audio_" in name],
                key=lambda x: int(x.split("_")[-1].split(".")[0])  # Extract index and sort
            )
            
            part_files = [
                pandas.read_json(archive.open(file)) for file in streaming_files
            ]
            
        streaming_history = pandas.concat(part_files, ignore_index=True)

    streaming_history = streaming_history[streaming_history['spotify_track_uri'].notnull()]

    useful_colls = [
        'ts',
		'ms_played',
		'master_metadata_track_name',
		'master_metadata_album_artist_name',
		'master_metadata_album_album_name',
		'spotify_track_uri'
	]

    streaming_history = streaming_history[useful_colls]
            
    streaming_history = streaming_history.rename(columns={
        'master_metadata_track_name': 'track_name',
        'master_metadata_album_artist_name': 'artist_name',
        'master_metadata_album_album_name': 'album_name',
        'spotify_track_uri': 'track_uri'
    })    

    return streaming_history

streaming_history = import_streaming_history()
