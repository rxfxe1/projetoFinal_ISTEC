import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="logo">
                Sushi Delight
            </div>
            <ul>
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/menu">Menu</Link>
                </li>
                <li>
                    <Link to="/reserve">Reserve</Link>
                </li>
                <li>
                    <Link to="/orders">Orders</Link>
                </li>
            </ul>
        </nav>
    );
};

export default Navbar;