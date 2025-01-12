USE publications;

SELECT a.au_id, a.au_lname, a.au_fname, COUNT(*) AS Titres
from publications.titleauthor ta
join publications.authors a on ta.au_id = a.au_id
join publications.titles t on ta.title_id = t.title_id
join publications.publishers p on t.pub_id = p.pub_id
GROUP bY a.au_id, a.au_lname, a.au_fname
ORDER BY Titres desc, au_id LIMIT 3;
