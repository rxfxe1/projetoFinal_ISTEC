import React from 'react';
import './Menu.css';

const Menu = () => {

    useEffect(() => {
        console.log('Menu component rendered');
        return () => {
            console.log('Menu component unmounted');
        };
    }, []);


    return (
        <div className="menu-container">
            <h2>Menu</h2>
            <div className='menu-list'>
                {/* Display menu items and prices here */}
                <div className='menu-item'>
                    <div className='item-name'>Sashimi Deluxe</div>
                    <div className='item-price'>$15/piece</div>
                </div>
                <div className='menu-item'>
                    <div className='item-name'>Dragon Roll</div>
                    <div className='item-price'>$10/piece</div>
                </div>
                {/* Add more items as needed */}
            </div>
        </div>
    );
};

export default Menu;