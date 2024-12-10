
## Importing Streaming history
%%[[2024-12-09]] @ 02:49%%

I've given it a quick trial and importing the streaming history straight from the zip archive to a pandas DataFrame is pretty quick and doesn't hog too much ram. 

The json files contain the following keys:
%% `['ts', 'platform', 'ms_played', 'conn_country', 'ip_addr', 'master_metadata_track_name', 'master_metadata_album_artist_name', 'master_metadata_album_album_name', 'spotify_track_uri', 'episode_name', 'episode_show_name', 'spotify_episode_uri', 'reason_start', 'reason_end', 'shuffle', 'skipped', 'offline', 'offline_timestamp', 'incognito_mode']` %%

| Key                                   | Description                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `'ts'`                                | This field is a timestamp indicating when the track stopped playing in UTC (Coordinated Universal Time). The order is year, month and day followed by a timestamp in military time username                                                                                                                                               |
| `'platform'`                          | This field is the platform used when streaming the track (e.g. Android OS, Google Chromecast).                                                                                                                                                                                                                                            |
| `'ms_played'`                         | This field is the number of milliseconds the stream was played.                                                                                                                                                                                                                                                                           |
| `'conn_country'`                      | This field is the country code of the country where the stream was played (e.g. SE - Sweden).                                                                                                                                                                                                                                             |
| `'ip_addr'`                           | This field contains the IP address logged when streaming the track. 4                                                                                                                                                                                                                                                                     |
| `'master_metadata_track_name'`        | This field contains the user agent used when streaming the track (e.g. a browser, like Mozilla Firefox, or Safari)                                                                                                                                                                                                                        |
| `'master_metadata_album_artist_name'` | This field is the name of the track.                                                                                                                                                                                                                                                                                                      |
| `'master_metadata_album_album_name'`  | This field is the name of the artist, band or podcast.                                                                                                                                                                                                                                                                                    |
| `'spotify_track_uri'`                 | This field is the name of the album of the track.                                                                                                                                                                                                                                                                                         |
| `'episode_name'`                      | A Spotify URI, uniquely identifying the track in the form of “spotify:track:<base-62 string>” A Spotify URI is a resource identifier that you can enter, for example, in the Spotify Desktop client’s search box to locate an artist, album, or track.                                                                                    |
| `'episode_show_name'`                 | This field contains the name of the episode of the podcast.                                                                                                                                                                                                                                                                               |
| `'spotify_episode_uri'`               | This field contains the name of the show of the podcast.  A Spotify Episode URI, uniquely identifying the podcast episode in the form of “spotify:episode:<base-62 string>” A Spotify Episode URI is a resource identifier that you can enter, for example, in the Spotify Desktop client’s search box to locate an episode of a podcast. |
| `'reason_start'`                      | This field is a value telling why the track started (e.g. “trackdone”)                                                                                                                                                                                                                                                                    |
| `'reason_end'`                        | This field is a value telling why the track ended (e.g. “endplay”). shuffle                                                                                                                                                                                                                                                               |
| `'shuffle'`                           | This field has the value True or False depending on if shuffle mode was used when playing the track. skipped                                                                                                                                                                                                                              |
| `'skipped'`                           | This field indicates if the user skipped to the next song offline                                                                                                                                                                                                                                                                         |
| `'offline'`                           | This field indicates whether the track was played in offline mode (“True”) or not (“False”).                                                                                                                                                                                                                                              |
| `'offline_timestamp'`                 | This field is a timestamp of when offline mode was used, if used.                                                                                                                                                                                                                                                                         |
| `'incognito_mode'`                    | This field indicates whether the track was played during a private session (“True”) or not (“False”).                                                                                                                                                                                                                                     |

of these I only need:
`['ts', 'ms_played', 'master_metadata_track_name', 'master_metadata_album_artist_name', 'master_metadata_album_album_name', 'spotify_track_uri']`
So can disregard the rest.

Podcasts have no values for:
`['master_metadata_track_name', 'master_metadata_album_artist_name', 'master_metadata_album_album_name', 'spotify_track_uri']`
but will have values in:
`['episode_name', 'episode_show_name', 'spotify_episode_uri']`
It should be easy enough to just purge any frames with no value for `'spotify_track_uri'`.

The raw `'ts'` could be converted into useful bins such as:
- `time_of_day` : half hour time of day bins int:0-47
- `day_of_week` : day of week int:0-6
- `date` : date YYYY-MM-DD

Or used as is with some `datetime` functions
