// src/components/MessageList.jsx
import React from 'react';
import ReactMarkdown from 'react-markdown';
import LoadingIndicator from './LoadingIndicator';

const MessageList = ({ messages, isLoading, isSearching }) => {
  // Add a safeguard to prevent mapping undefined
  if (!messages || !Array.isArray(messages)) {
    return <div className="message-list">No messages to display</div>;
  }

  const formatTime = (timestamp) => {
    return new Date(timestamp).toLocaleTimeString([], { 
      hour: '2-digit', 
      minute: '2-digit' 
    });
  };

  return (
    <div className="message-list">
      {messages.map((message) => (
        <div 
          key={message.id} 
          className={`message ${message.sender === 'user' ? 'user-message' : 'bot-message'} ${message.isError ? 'error-message' : ''}`}
        >
          <div className="message-content">
            <div className="message-text">
              <ReactMarkdown>
                {typeof message.text === "string" ? message.text : JSON.stringify(message.text)}
              </ReactMarkdown>
            </div>   
            {message.image && (
              <div className="message-image-container">
                <img 
                  src={message.image} 
                  alt="Uploaded content" 
                  className="message-image" 
                />
              </div>
            )}
            <div className="message-timestamp">{formatTime(message.timestamp)}</div>
          </div>
        </div>
      ))}
      
      {isLoading && (
        <div className={`message bot-message loading-message`}>
          <div className="message-content">
            {isSearching ? (
              <LoadingIndicator />
            ) : (
              <div className="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default MessageList;