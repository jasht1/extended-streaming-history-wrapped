
## Investigating methods for acquiring genre information
%%[[2024-12-12]] @ 02:23%%

I have the following fields in the dataset: 
- `['ts', 'ms_played', 'track_name', 'artist_name', 'album_name', 'track_uri']`

More interesting insights are to be had based on "genre", this will require some sort of API call. Depending on diversity of the streaming history that could be allot of API calls. 

### Spotify API
%%[[2024-12-12]] @ 02:29%%

There is a python library called `spotipy` with pre-built methods for authentication and calls for all the end points. 

#### Authentication

##### Dev APP Auth codes
It would be a bit of a pain to get users to generate and enter their own auth codes and I don't want to give out mine. 
[Guide](https://developer.spotify.com/documentation/web-api/concepts/apps)

##### PKCE
It seem's like PKCE could be a better option as it only requires `client_id` which is in [[my_spotify_data.zip]] and then lets the user accept or deny through their Spotify client. 
[Guide](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow)

#### Relevant end point

The [[#Spotify API]] has an end point called `recommendation_genre_seeds()` but [the documentation](https://developer.spotify.com/documentation/web-api/reference/get-recommendation-genres) is a little sparse. It seems to me like it just provides the genres relevant to to the current listening session, but I will have to test it out.