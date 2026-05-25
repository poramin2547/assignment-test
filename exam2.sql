-- หา Top 3 ร้านอาหารในแต่ละ category
-- โดยดูจาก Average Order Value (AOV)
-- เฉพาะออเดอร์ที่ delivered ในเดือนปัจจุบัน

WITH ranked_restaurants AS (
    SELECT
        r.restaurant_id,
        r.restaurant_name,
        r.category,

        -- ค่าเฉลี่ยยอดต่อออเดอร์
        COALESCE(AVG(o.total_amount), 0) AS aov,

        -- จัดอันดับร้านในแต่ละ category
        RANK() OVER (
            PARTITION BY r.category
            ORDER BY AVG(o.total_amount) DESC
        ) AS rank_num

    FROM restaurants r
    LEFT JOIN orders o
        ON r.restaurant_id = o.restaurant_id
        AND o.status = 'delivered'
        AND YEAR(o.order_date) = YEAR(CURDATE())
        AND MONTH(o.order_date) = MONTH(CURDATE())

    GROUP BY r.restaurant_id, r.restaurant_name, r.category
)

SELECT *
FROM ranked_restaurants
WHERE rank_num <= 3;