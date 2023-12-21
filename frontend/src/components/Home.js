import React, { useEffect } from 'react';
import './Home.css';

const Home = () => {

    useEffect(() => {
        console.log('Home component rendered');
        return () => {
            console.log('Home component unmounted');
        };
    }, []);

    
    return (
        <div className="home-container">
            <header>
                <h1>Welcome to Sushi Delight!</h1>
            </header>

            <section className="features">
                <div className="feature">
                    <h2>Explore Our Sushi Menu</h2>
                    <p>Delicious and fresh sushi prepared with the finest ingredients.</p>
                </div>
                
                <div className="feature">
                    <h2>Place Your Order</h2>
                    <p>Choose your favorite sushi and place your order online.</p>
                </div>

                <div className="feature">
                    <h2>Reserve a Table</h2>
                    <p>Book a table for an unforgettable dining experience.</p>
                </div>
            </section>

            <section className="about-us">
                <h2>About Us</h2>
                <p>
                    Sushi Delight is commited to providing the best sushi experience in town.
                </p>
            </section>
        </div>
    );
};

export default Home;