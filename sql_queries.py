# create = "CREATE TABLE IF NOT EXISTS {table}({cols})"
drop = "DROP TABLE IF EXISTS {table}"

# _srl = 'SERIAL'
# _int = 'INTEGER'
# _txt = 'TEXT'
# _ts = 'TIMESTAMP'
# _vc = 'VARCHAR'

# def nn(dt):
#     return '{} NOT NULL'.format(dt)

# def fk(dt)
#     if fk:
#         query += ''.join([ 'FOREIGN KEY ({}) references {} {}'.format(*f) for f in fk ])
#     return query

# def write_col(c, dt, pk)
#     if c == pk:
#         return '{} {} PRIMARY KEY\n'.format(c, dt)
#     else:
#         return '{} {}\n'.format(c, dt)

# def write_cols(colDict, pk=None):
#     return ','.join([ write_col(k,v,pk) for k,v in colDict.items() ])

# def write_create(table, cols, pk=None)
#     return add_foreign_key(create.format(table=table, write_cols(colDict, pk=pk)))

# DROP TABLES

songplay_table_drop = drop.format(table='songplays')
user_table_drop =  drop.format(table='users')
song_table_drop =  drop.format(table='songs')
artist_table_drop =  drop.format(table='artists')
time_table_drop =  drop.format(table='time')

# CREATE TABLES

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
    user_id int primary key,
    first_name varchar,
    last_name varchar,
    gender char(1),
    level varchar
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
    artist_id varchar primary key,
    name varchar,
    location varchar,
    latitude float4,
    longitude float4
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
    song_id varchar primary key,
    title varchar,
    artist_id varchar,
    year int,
    duration float4
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
    start_time timestamp primary key,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
)
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
    songplay_id serial primary key,
    start_time timestamp references time (start_time),
    user_id int references users (user_id),
    level varchar,
    song_id varchar references songs (song_id),
    artist_id varchar references artists (artist_id),
    session_id int,
    location varchar,
    user_agent varchar
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users(user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE set level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs(song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, a.artist_id
FROM songs as s, artists as a
WHERE s.artist_id = a.artist_id and s.title=%s and a.name = %s and s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create ]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]