pragma solidity ^0.5.0;

contract createProduct{
     struct product{
        string productId;
        string productName;
        string Category;
        uint price;
        string description;
        }
 mapping (string => product) products;
 product[] public allProducts;


 function addProduct(string memory _productId, string memory _productName, string memory _category, uint _price, string memory _description) public {
 product memory product = product(_productId, _productName, _category, _price, _description);
       products[_productId].productId= _productId;
       products[_productId].productName= _productName;
       products[_productId].Category= _category;
       products[_productId].description= _description;
       products[_productId].price= _price;
       allProducts.push(product);

     }

}