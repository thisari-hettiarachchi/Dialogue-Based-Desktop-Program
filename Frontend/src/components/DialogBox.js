import React, { useState } from 'react';
import axios from 'axios';

const DialogBox = () => {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async () => {
    const res = await axios.post('http://127.0.0.1:5000/ask', { question });
    setResponse(res.data.answer);
  };

  return (
    <div>
      <h2>Ask a Programming Question</h2>
      <input 
        type="text" 
        value={question} 
        onChange={(e) => setQuestion(e.target.value)} 
        placeholder="Enter a programming concept..." 
      />
      <button onClick={handleSubmit}>Ask</button>
      <p>Response: {response}</p>
    </div>
  );
};

export default DialogBox;
