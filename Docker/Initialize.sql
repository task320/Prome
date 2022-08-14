-- setting
CREATE schema prome;
SET search_path TO prome;
ALTER database "test_db" SET search_path TO prome;
ALTER DATABASE test_db SET timezone TO 'Asia/Tokyo';


-- tables
create table users(
    id serial,
    auth_string varchar(512),
    create_at timestamp,
    update_at timestamp,
    primary key (id)
);

CREATE TABLE contents (
  id serial,
  title varchar(128),
  tags varchar(32)[],
  content text,
  users_id int references users(id),
  upload_at timestamp,
  update_at timestamp,
  version int,
  primary key (id)
);


-- add application user  userid:test password:test
 insert into users (auth_string, create_at, update_at) values ('d40d0b2f6540e17654edfa3a0d0ab43abcd7d653926bfa832052d2dab4a627a9', current_timestamp, current_timestamp);
 