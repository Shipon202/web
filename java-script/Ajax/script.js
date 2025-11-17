async function getProducts() {
    let url = 'https://crud.teamrabbil.com/api/v1/ReadProduct';
    let response = await axios.get(url);
    // console.log(response.data);
    let products =response.data['data'];
    products.forEach((item) => {
        document.getElementById('productList').innerHTML +=(`
            <tr>
            <td> ${item['ProductName']}</td>
            <td> ${item['ProductCode']}</td>
            <td> ${item['UnitPrice']}</td>
            <td> ${item['Qty']}</td>
            <td> ${item['TotalPrice']}</td>
            <td> <button onclick="deleteProduct('${item['_id']}')">Delete</button> </td>
            <td> <button onclick="goToudate('${item['_id']}')">Edit</button> </td>
            </tr>
            `)
        
    });
}
getProducts();

//delete product

async function deleteProduct(id){
    let url = `https://crud.teamrabbil.com/api/v1/DeleteProduct/${id}`;
    let response = await axios.get(url);
    document.getElementById('productList').innerHTML = '';
    getProducts();

}
function goToudate(id){
    window.location = `update.html?id=${id}`;
}
async function addNewProduct(){
    let ProductName =document.getElementById('ProductName').value;
    let ProductCode =document.getElementById('ProductCode').value;
    let ProductImg =document.getElementById('ProductImg').value;
    let UnitPrice =document.getElementById('UnitPrice').value;
    let Qty =document.getElementById('Qty').value;
    let TotalPrice =document.getElementById('TotalPrice').value;
    let obj = {
        
            "Img":ProductImg,
            "ProductCode":ProductCode,
            "ProductName":ProductName,
            "Qty":Qty,
            "TotalPrice":TotalPrice,
            "UnitPrice":UnitPrice
        
        };
    let url = 'https://crud.teamrabbil.com/api/v1/CreateProduct';
    let response = await axios.post(url,obj);
    window.location="index2.html";
}