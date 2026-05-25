WITH ranked_restaurants AS (

    SELECT
        r.restaurant_id,
        r.restaurant_name,
        r.category,

        COALESCE(AVG(o.total_amount), 0) AS aov,

        RANK() OVER (
            PARTITION BY r.category
            ORDER BY COALESCE(AVG(o.total_amount), 0) DESC
        ) AS ranking

    FROM restaurants r

    LEFT JOIN orders o
        ON r.restaurant_id = o.restaurant_id
        AND o.status = 'delivered'
        AND YEAR(o.order_date) = YEAR(CURRENT_DATE)
        AND MONTH(o.order_date) = MONTH(CURRENT_DATE)

    GROUP BY
        r.restaurant_id,
        r.restaurant_name,
        r.category
)

SELECT
    restaurant_id,
    restaurant_name,
    category,
    aov,
    ranking

FROM ranked_restaurants

WHERE ranking <= 3;