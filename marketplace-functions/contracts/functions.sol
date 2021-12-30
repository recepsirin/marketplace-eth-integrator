pragma solidity ^0.5.4;
contract Functions {

   address payable public owner;
   constructor() public {
     owner=msg.sender;
          }

     uint id;
     uint purchaseId;

   struct seller {
     string name;
     address addr;
     uint bankGuaraantee;
     bool bgPaid;
     }
   struct product{
        string productId;
        string productName;
        string Category;
        uint price;
        string description;
        address payable seller;
        bool isActive;
           }
    struct ordersPlaced {
        string productId;
        uint purchaseId;
        address orderedBy;
           }
    struct sellerShipment {
        string productId;
        uint purchaseId;
        string shipmentStatus;
        string deliveryAddress;
        address  payable orderedBy;
        bool isActive;
        bool isCanceled;
            }
    struct orders{
        string productId;
        string orderStatus;
        uint purchaseId;
        string shipmentStatus;
            }
  mapping(address=> seller) public sellers;
  mapping (string => product) products;
  product[] public allProducts;
  mapping (address=> ordersPlaced[]) sellerOrders;
  mapping (address=> mapping(uint=>sellerShipment))sellerShipments;
  mapping (address=>orders[]) userOrders;



function cancelOrder(string memory _productId, uint _purchaseId)  public payable {
      sellerShipments[products[_productId].seller][_purchaseId].shipmentStatus= "Order Canceled By Buyer, Payment will Be  Refunded";
      sellerShipments[products[_productId].seller][_purchaseId].isCanceled= true;
      sellerShipments[products[_productId].seller][_purchaseId].isActive= false;
             }

function updateShipment(uint _purchaseId, string memory _shipmentDetails) public {
      sellerShipments[msg.sender][_purchaseId].shipmentStatus= _shipmentDetails;
                    }

function getOrdersPlaced(uint _index) public view returns(string memory, uint, address, string memory) {
      return(sellerOrders[msg.sender][_index].productId, sellerOrders[msg.sender][_index].purchaseId, sellerOrders[msg.sender][_index].orderedBy, sellerShipments[msg.sender][sellerOrders[msg.sender][_index].purchaseId].shipmentStatus);
              }
function getShipmentDetails(uint _purchaseId) public view returns(string memory,string memory,address,string memory) {
      return(sellerShipments[msg.sender][_purchaseId].productId, sellerShipments[msg.sender][_purchaseId].shipmentStatus, sellerShipments[msg.sender][_purchaseId].orderedBy,sellerShipments[msg.sender][_purchaseId].deliveryAddress);
             }

}