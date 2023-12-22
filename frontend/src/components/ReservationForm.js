import React, { useState } from 'react';

const ReservationForm = () => {
    const [name, setName] = useState('');
    const [phone, setPhone] = useState('');
    const [table, setTable] = useState('');
    const [date, setDate] = useState('');
    const [time, setTime] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Handle form submission (connect to the server)
        console.log('Reservation submitted:', { name, phone, table, date, time });
    };

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
