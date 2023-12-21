import React from 'react';
import './Orders.css';

const Orders = () => {

    useEffect(() => {
        console.log('Orders component rendered');
        return () => {
            console.log('Orders component unmounted');
        };
    }, []);


    return (
        <div className="orders-container">
            <h2>Your Orders</h2>
            <div className="order-list">
                {/*  */}
            </div>
        </div>
    )
}

export default Orders;