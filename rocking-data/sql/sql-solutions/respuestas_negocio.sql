-- /* EJERCICIO 1 */
SELECT Orders.CustomerID AS "Customer ID",
	(Customers.CustomerName + ' ' + Customers.CustomerLastName) AS "Full Name",
	Customers.CustomerBirthdate AS 'Birthdate',
	-- Orders.OrderDate,
	SUM(OrderDetails.Quantity) AS 'Total Sales'
FROM Items
	INNER JOIN (
		(
			Customers
			INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
		)
		INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
	) ON Items.ItemID = OrderDetails.ItemID
WHERE (
		Orders.OrderDate BETWEEN '2020-01-01' AND '2020-01-31'
	)
	AND (
		DAY(Customers.CustomerBirthdate) = DAY(GETDATE())
		AND MONTH(Customers.CustomerBirthdate) = MONTH(GETDATE()) 
	)
GROUP BY Orders.CustomerID,
	(Customers.CustomerName + ' ' + Customers.CustomerLastName),
	Customers.CustomerBirthdate
	-- Orders.OrderDate
HAVING SUM(OrderDetails.Quantity) > 1500 
GO

	/* EJERCICIO 2 */
SELECT "Month",
-- "Sales Rank",
"Year",
"Full Name",
"Number of Sales",
"Total Sales",
"Gross Total"
FROM (
		SELECT MONTH(Orders.OrderDate) AS "Month#",
			DATENAME(MONTH, Orders.OrderDate) AS "Month",
			DATENAME(YEAR, Orders.OrderDate) AS "Year",
			(
				Customers.CustomerName + ' ' + Customers.CustomerLastName
			) AS "Full Name",
			ROW_NUMBER() OVER (
				PARTITION BY MONTH(Orders.OrderDate)
				ORDER BY SUM(Items.UnitPrice * OrderDetails.Quantity) DESC
			) AS "Sales Rank",
			SUM(OrderDetails.Quantity) AS "Total Sales",
			COUNT(OrderDetails.OrderID) AS "Number of Sales",
			(
				SUM(Items.UnitPrice * OrderDetails.Quantity)
			) AS "Gross Total"
		FROM Categories
			INNER JOIN (
				Items
				INNER JOIN (
					(
						Customers
						INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
					)
					INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
				) ON Items.ItemID = OrderDetails.ItemID
			) ON Items.CategoryName = Categories.CategoryName
		WHERE (
				datediff(m, Orders.OrderDate, '2020-12-31') between 0 and 12
			)
			AND Categories.CategoryName = 'Celulares'
		GROUP BY MONTH(Orders.OrderDate),
			DATENAME(MONTH, Orders.OrderDate),
			DATENAME(YEAR, Orders.OrderDate),
			(
				Customers.CustomerName + ' ' + Customers.CustomerLastName
			)
	) ranks
WHERE "Sales Rank" <= 5
ORDER BY "Month#"

	/* EJERCICIO 3 */
	/* Creating procedure */
DROP PROCEDURE IF EXISTS dbo.registerItemState
GO

CREATE PROCEDURE registerItemState
AS
BEGIN
		DROP TABLE IF EXISTS dbo.ItemsState
    SELECT Items.ItemID, Items.ItemName, Items.Discontinued 
    INTO ItemsState 
    FROM Items
END
