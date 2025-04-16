// src/components/ChatInterface.jsx
import React, { useState, useEffect, useRef } from 'react';
import MessageList from './MessageList';
import MessageInput from './MessageInput';
import { sendMessage } from '../services/api';

const ChatInterface = () => {
  const [messages, setMessages] = useState([
    {
      id: 1,
      text: "Hello! I'm Vesta, your real estate assistant. How can I help you today?",
      sender: 'bot',
      timestamp: new Date(),
    },
  ]);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSendMessage = async (text, image = null) => {
    if (!text && !image) return;

    // Add user message to chat
    const userMessage = {
      id: messages.length + 1,
      text: text || "",
      sender: 'user',
      timestamp: new Date(),
      image: image ? URL.createObjectURL(image) : null,
    };
    
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setLoading(true);

    try {
      // Send message to API with both text and image if available
      const response = await sendMessage(text, image);

      // Add bot response to chat
      const botMessage = {
        id: messages.length + 2,
        text: response.message || "I'm processing your request...",
        sender: 'bot',
        timestamp: new Date(),
      };
      
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      // Add error message
      const errorMessage = {
        id: messages.length + 2,
        text: "Sorry, I'm having trouble processing your request right now. Please try again.",
        sender: 'bot',
        timestamp: new Date(),
        isError: true,
      };
      
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-interface">
      <div className="messages-container">
        <MessageList messages={messages} />
        <div ref={messagesEndRef} />
      </div>
      <MessageInput onSendMessage={handleSendMessage} isLoading={loading} />
    </div>
  );
};

export default ChatInterface;