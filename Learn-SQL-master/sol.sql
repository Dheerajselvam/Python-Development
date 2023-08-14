use record_company;

select name from bands;

select * from albums where release_year is not null
order by release_year limit 1;

select distinct(b.name) from bands as b join albums as a on
b.id = a.band_id;

select distinct(b.name) from bands as b left join albums as a on
b.id = a.band_id where a.id is null;

select a.name, a.release_year, sum(s.lenght) as duration 
from albums as a join songs as s
on a.id = s.alumb_id
group by s.alumb_id
order by duration desc
limit 1;

update albums  set release_year = 1986
where id = 4;

insert into bands (name) values ('Thuppaki');

select * from bands;

delete from bands where id = 8;

select * from bands;

select avg(length) from songs;

select a.name, a.release_year, max(s.length) from albums as a
join songs as s on a.id = s.album_id
group by s.album_id;

select b.name, count(s.id) from bands as b
join albums as a on b.id = a.band_id
join songs as s on a.id = s.album_id
group by a.band_id;




