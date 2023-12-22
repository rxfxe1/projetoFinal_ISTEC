import React, { useState } from 'react';
import axios from 'axios';

const ReservationForm = () => {
    const [name, setName] = useState('');
    const [phone, setPhone] = useState('');
    const [table, setTable] = useState('');
    const [date, setDate] = useState('');
    const [time, setTime] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/reservations/', {
                name, 
                phone,
                table, 
                date, 
                time,
            });
            console.log('Reservation submitted successfully:', response.data);
        } catch (error) {
            console.error('Error submitting reservation:', error);
        }
    }

    return (
        <div className="reservation-form">
            <h2>Reserve a table</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Name:
                    <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
                </label>
                <label>
                    Phone Number:
                    <input type="tel" value={phone} onChange={(e) => setPhone(e.target.value)} />
                </label>
                <label>
                    Table Number:
                    <select value={table} onChange={(e) => setTable(e.target.value)}>
                        <option value="">Select Table</option>
                        <option value="1">Table 1</option>
                        <option value="2">Table 2</option>
                        {/* Add more options as needed */}
                    </select>
                </label>
                <label>
                    Date:
                    <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
                </label>
                <label>
                    Time:
                    <input type="time" value={time} onChange={(e) => setTime(e.target.value)} />
                </label>
                
                <button type="submit">Reserve Now</button>
            </form>
        </div>
    );
};

export default ReservationForm;
