import spotipy
from datetime import datetime, timedelta

def check_or_create_playlist(sp, playlist_id, playlist_name, public=True):
    """
    Verifica si existe una playlist por su ID. Si no existe, crea una nueva.
    Argumentos:
    - sp: Instancia autenticada de spotipy.Spotify
    - playlist_id: ID de la playlist a verificar o crear
    - playlist_name: Nombre de la playlist a crear si no se encuentra
    - public: Booleano para establecer la playlist como pública o privada
    Devuelve:
    - ID de la playlist
    """
    offset = 0
    while True:
        try:
            playlists = sp.current_user_playlists(limit=50, offset=offset)
        except Exception as e:
            print(f"Error al recuperar las playlists: {e}")
            return None

        for playlist in playlists['items']:
            if playlist['id'] == playlist_id:
                return playlist['id']
        
        if not playlists['next']:
            break
        offset += 50

    # Si no se encuentra, crea una nueva playlist
    try:
        new_playlist = sp.user_playlist_create(user=sp.me()['id'], name=playlist_name, public=public)
        return new_playlist['id']
    except Exception as e:
        print(f"Error al crear la playlist: {e}")
        return None

def update_playlist(sp, playlist_id, clean_playlist=False):
    generos = ['k-pop', 'korean r&b', 'k_rap', 'k-pop girl group']
    hace_tres_meses = (datetime.now() - timedelta(days=360)).strftime('%Y-%m-%d')
    resultados = sp.new_releases(limit=50)
    track_uris = []

    try:
        while resultados:
            albums = resultados['albums']
            print(f"Revisando {len(albums['items'])} álbumes")  # Mensaje de depuración
            for lanzamiento in albums['items']:
                id_album = lanzamiento['id']
                detalles_album = sp.album(id_album)
                nombre_album = detalles_album['name']  # Obtener el nombre del álbum
                fecha_lanzamiento = detalles_album['release_date']
                ids_artistas = [artista['id'] for artista in detalles_album['artists']]
                
                # Obtener géneros de todos los artistas en el álbum
                generos_artistas = []
                for id_artista in ids_artistas:
                    detalles_artista = sp.artist(id_artista)
                    generos_artistas.extend(detalles_artista['genres'])
                
                # Mensaje de depuración con el nombre del álbum
                print(f"Álbum '{nombre_album}' géneros de artistas: {generos_artistas}, lanzado en {fecha_lanzamiento}")
                
                # Verificar si el género de algún artista coincide con los géneros deseados
                if fecha_lanzamiento >= hace_tres_meses and any(genero in generos_artistas for genero in generos):
                    pistas = sp.album_tracks(id_album)
                    for pista in pistas['items']:
                        print(f"Añadiendo pista '{pista['name']}' del álbum '{nombre_album}'")  # Mensaje de depuración
                    track_uris.extend([pista['uri'] for pista in pistas['items']])
            
            # Si hay más páginas de álbumes, continuar con la siguiente
            if albums['next']:
                resultados = sp.next(albums)
            else:
                break

        if track_uris:
            if clean_playlist:
                sp.playlist_replace_items(playlist_id, [])
            sp.playlist_add_items(playlist_id, track_uris)
            print(f'Se añadieron {len(track_uris)} pistas a la playlist.')
        else:
            print('No se encontraron pistas nuevas que coincidan con los criterios.')
    except Exception as e:
        print(f"Error al actualizar la playlist: {e}")



