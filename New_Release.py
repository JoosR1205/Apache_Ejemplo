from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from functions import check_or_create_playlist, update_playlist
from spotify_authentication import authenticate_spotify

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'spotify_playlist_manager',
    default_args=default_args,
    description='Manage Spotify playlists',
    schedule_interval=timedelta(days=1),
)

def manage_playlist():
    sp = authenticate_spotify()
    playlist_name = "New K-Releases"
    playlist_description = "Daily new releases for selected genres."
    playlist_id = "5QJ4EX0B8gX3eJ0FGzqHTo?si=e91515c5c3ac4612"  # Esto podría cambiar a un argumento o variable dinámica

    playlist_id = check_or_create_playlist(sp, playlist_id, playlist_name, public=True) 
    update_playlist(sp, playlist_id)

manage_playlist_task = PythonOperator(
    task_id='manage_playlist',
    python_callable=manage_playlist,
    dag=dag,
)

manage_playlist_task
