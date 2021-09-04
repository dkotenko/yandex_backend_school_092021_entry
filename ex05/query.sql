select DATE(date, 'start of month') monthDate, description, statistic.name name, b.name brand_name, c.name category_name,  sum(shows) sum_shows, sum(clicks) sum_clicks, sum(orders) sum_orders, SUM(gmv) sum_gmv
from statistic
LEFT JOIN brands b on statistic.brand_id = b.id
LEFT JOIN categories c on statistic.category_id = c.id

WHERE category_name != 'Варочные панели' AND category_name != 'Садовые измельчители'
AND brand_name != 'Apple' AND brand_name != 'Samsung'
AND statistic.shows >= statistic.clicks AND statistic.clicks >= statistic.orders
     --(SELECT date, sum(shows) sh, sum(clicks) cl, sum(orders) ord FROM statistic GROUP BY date) t WHERE  t.sh >= t.cl AND t.cl >= t.ord)
AND date >= '2021-04-01' and date <= '2021-07-31'
GROUP BY monthDate, description, statistic.name, category_name, brand_name
ORDER BY monthDate ASC, gmv DESC
LIMIT 100;