import { useState } from 'react';
import axios from 'axios';

function App() {
  const [order, setOrder] = useState({
    product_id: 1,
    quantity: 1,
    customer_name: '',
    delivery_address: ''
  });

  const handleChange = (e) => {
    setOrder({ ...order, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/order/', order);
      alert(response.data.message);
    } catch (error) {
      alert('Error placing order');
    }
  };

  return (
    <div>
      <h1>Order Ceramic Products</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" name="customer_name" placeholder="Your Name" onChange={handleChange} required />
        <input type="text" name="delivery_address" placeholder="Delivery Address" onChange={handleChange} required />
        <button type="submit">Place Order</button>
      </form>
    </div>
  );
}

export default App;
