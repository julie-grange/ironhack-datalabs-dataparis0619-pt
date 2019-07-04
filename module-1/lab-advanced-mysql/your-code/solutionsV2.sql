{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf400
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 -- Challenge 1\
-- Calculate the royalties of each sales for each author\
\
USE publications;\
\
SELECT a.au_id, t.title_id, t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 as royalties\
from authors a\
left join titleauthor ta on a.au_id = ta.au_id\
left join titles t on ta.title_id = t.title_id\
left join sales s on t.title_id = s.title_id\
;\
\
-- Aggregate the total royalties for each title for each author\
\
select author_ID, title_ID, SUM(royalties) as Total\
from (\
	SELECT a.au_id as author_ID, t.title_id as title_ID, t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 as royalties\
	from authors a\
	left join titleauthor ta on a.au_id = ta.au_id\
	left join titles t on ta.title_id = t.title_id\
	left join sales s on t.title_id = s.title_id\
) itermdT\
GROUP by author_ID, title_ID\
ORDER by Total desc \
;\
\
\
-- Calculate the total profits of each author\
\
Select author_ID, title_ID, SUM(advance + royalties) as profits\
from (\
	SELECT a.au_id as author_ID, t.title_id as title_ID, t.advance as advance, t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 as royalties\
	from authors a\
	left join titleauthor ta on a.au_id = ta.au_id\
	left join titles t on ta.title_id = t.title_id\
	left join sales s on t.title_id = s.title_id\
) itermdT\
GROUP by author_ID, title_ID\
ORDER by profits desc  LIMIT 3;\
\
\
-- Challenge 2\
CREATE TEMPORARY TABLE profit_authors\
Select author_ID, title_ID, SUM(advance + royalties) as profits\
from (\
	SELECT a.au_id as author_ID, t.title_id as title_ID, t.advance as advance, t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 as royalties\
	from authors a\
	left join titleauthor ta on a.au_id = ta.au_id\
	left join titles t on ta.title_id = t.title_id\
	left join sales s on t.title_id = s.title_id\
) itermdT\
GROUP by author_ID, title_ID\
ORDER by profits desc;\
\
Select author_ID, title_ID, profits\
from profit_authors\
order by profits desc LIMIT 3;\
\
-- Challenge 3\
\
CREATE TABLE most_profiting_authorsV3\
Select author_ID, title_ID, SUM(advance + royalties) as profits\
from (\
	SELECT a.au_id as author_ID, t.title_id as title_ID, t.advance as advance, t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 as royalties\
	from authors a\
	left join titleauthor ta on a.au_id = ta.au_id\
	left join titles t on ta.title_id = t.title_id\
	left join sales s on t.title_id = s.title_id\
) itermdT\
GROUP by author_ID, title_ID\
ORDER by profits desc;\
\
Select author_ID, title_ID, profits\
from most_profiting_authorsV3\
order by profits desc LIMIT 3;\
}