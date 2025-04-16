// src/components/MessageInput.jsx
import React, { useState, useRef } from 'react';
import { FaPaperPlane, FaImage, FaTimes } from 'react-icons/fa';
import ImageUpload from './ImageUpload';

const MessageInput = ({ onSendMessage, isLoading }) => {
  const [message, setMessage] = useState('');
  const [image, setImage] = useState(null);
  const [showImageUpload, setShowImageUpload] = useState(false);
  const textareaRef = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim() || image) {
      onSendMessage(message.trim(), image);
      setMessage('');
      setImage(null);
      setShowImageUpload(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  const handleImageSelect = (selectedImage) => {
    setImage(selectedImage);
    setShowImageUpload(false);
  };

  const removeImage = () => {
    setImage(null);
  };

  const adjustTextareaHeight = () => {
    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = 'auto';
      textarea.style.height = `${Math.min(textarea.scrollHeight, 120)}px`;
    }
  };

  return (
    <div className="message-input-container">
      {image && (
        <div className="selected-image-preview">
          <img 
            src={URL.createObjectURL(image)} 
            alt="Selected" 
            className="preview-image" 
          />
          <button 
            className="remove-image-btn" 
            onClick={removeImage}
            aria-label="Remove image"
          >
            <FaTimes />
          </button>
        </div>
      )}
      
      {showImageUpload && (
        <ImageUpload 
          onImageSelect={handleImageSelect}
          onCancel={() => setShowImageUpload(false)}
        />
      )}
      
      <form className="input-form" onSubmit={handleSubmit}>
        <textarea
          ref={textareaRef}
          className="message-input"
          value={message}
          onChange={(e) => {
            setMessage(e.target.value);
            adjustTextareaHeight();
          }}
          onKeyDown={handleKeyDown}
          placeholder="Type your message..."
          rows={1}
          disabled={isLoading}
        />
        
        <button
          type="button"
          className="image-button"
          onClick={() => setShowImageUpload(!showImageUpload)}
          disabled={isLoading}
          aria-label="Upload image"
        >
          <FaImage />
        </button>
        
        <button
          type="submit"
          className="send-button"
          disabled={isLoading || (!message.trim() && !image)}
          aria-label="Send message"
        >
          <FaPaperPlane />
        </button>
      </form>
    </div>
  );
};

export default MessageInput;