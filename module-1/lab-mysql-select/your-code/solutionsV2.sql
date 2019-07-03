
-- Challenge 1
SELECT a.au_id, a.au_lname, a.au_fname, t.title, p.pub_name
from publications.titleauthor ta
join publications.authors a on ta.au_id = a.au_id
join publications.titles t on ta.title_id = t.title_id
join publications.publishers p on t.pub_id = p.pub_id;

-- Challenge 2
SELECT a.au_id, a.au_lname, a.au_fname, p.pub_name, COUNT(*) AS Titres
from publications.titleauthor ta
join publications.authors a on ta.au_id = a.au_id
join publications.titles t on ta.title_id = t.title_id
join publications.publishers p on t.pub_id = p.pub_id
GROUP bY a.au_id, a.au_lname, a.au_fname, p.pub_name;


-- Challenge 3
SELECT a.au_id, a.au_lname, a.au_fname, COUNT(ta.title_id) AS Titres
from publications.titleauthor ta
right join publications.authors a on ta.au_id = a.au_id
GROUP bY a.au_id, a.au_lname, a.au_fname
ORDER BY Titres desc, au_id LIMIT 3;

-- Challenge 4
select
a.au_lname, a.au_fname, t.title, sum(t.ytd_sales) as Sales
from authors a
left join titleauthor ta on ta.au_id = a.au_id
left join titles t on t.title_id = ta.title_id
group by a.au_id, t.title
order by Sales desc
;

