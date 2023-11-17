let item={
    name:'phone',
    price: 25000,
    quantity:1,
    categories:['elect','phones'],
    dimension:{
        length: 7.1,
        breadth: 5,
        height: 10
    }
}
console.log(item)

let item2= new Object();

item2.name = 'charger'
item2.price = 700
item2.quantity = 1

console.log(item2)
console.log(item.price)
item.price = 240000
console.log(item.price)

item.returnable = true
console.log(item)

let key = 'price'
item[key] = 27500
console.log(item[key])

item={
    name:'phone',
    price: 25000,
    quantity:1,
    buy: function(){
        console.log('item added to cart')
    },
    addtolist(){
        console.log('item added to list')
    }

}

item.buy()
item.addtolist()