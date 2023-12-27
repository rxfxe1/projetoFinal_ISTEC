import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/token/', {
                username,
                password,
            });
            console.log('Login successful:', response.data);
            // Handle succefull login (e.g., redirect)
        } catch (error) {
            console.error('Error logging in:', error);
        }
    }

    return (
        <div className="Login-form">
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
                </label>
                <label>
                    Password:
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                </label>
                <button type="submit">Log In</button>
            </form>
            <div>
                <p>Don't have an account yet? <Link to="/register">Register</Link></p>
            </div>
        </div>
    );
};

export default Login;