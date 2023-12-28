import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ReservationForm = () => {
    const [name, setName] = useState('');
    const [phone, setPhone] = useState('');
    const [numPeople, setNumPeople] = useState('');
    const [table, setTable] = useState('');
    const [date, setDate] = useState('');
    const [time, setTime] = useState('');

    const [tables, setTables] = useState([]);

    useEffect(() => {
        // Fetch tables from Django API
        const fetchTables = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/tables/');
                setTables(response.data);
            } catch (error) {
                console.error('Error fetching tables:', error);
            }
        };

        fetchTables();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/reservations/', {
                name, 
                phone,
                num_people: numPeople,
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
                    Phone number:
                    <input type="tel" value={phone} onChange={(e) => setPhone(e.target.value)} />
                </label>
                <label>
                    Number of people:
                    <input
                        type="number"
                        value={numPeople}
                        onChange={(e) => setNumPeople(Math.max(1, e.target.value))}
                        min="1"
                    />
                </label>
                <label>
                    Table:
                    <select value={table} onChange={(e) => setTable(e.target.value)} >
                        <option value="">Select Table</option>
                        {tables.map((table) => (
                            <option key={table.id} value={table.id}>
                                {`Table ${table.number} - Capacity:P ${table.capacity}`}
                            </option>
                        ))}
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
