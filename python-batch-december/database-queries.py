Show databases;
create database afternoon;

use afternoon;

drop database afternoon;

show tables;

create table ContactUs(UserName varchar(120), Age int, Email varchar(120), Message text);

select * from ContactUs;

insert into ContactUs values("hlo", 21, "hlo@gmail.com", "this is hlo message");
