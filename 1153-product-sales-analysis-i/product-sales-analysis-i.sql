select Product.product_name , Sales.year, Sales.price from Product
join Sales on Product.product_id = Sales.product_id;