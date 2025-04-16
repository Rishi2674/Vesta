// src/components/ImageUpload.jsx
import React, { useRef, useState } from 'react';
import { FaUpload, FaTimes } from 'react-icons/fa';

const ImageUpload = ({ onImageSelect, onCancel }) => {
  const fileInputRef = useRef(null);
  const [dragActive, setDragActive] = useState(false);
  const [previewImage, setPreviewImage] = useState(null);

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      processFile(e.dataTransfer.files[0]);
    }
  };

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      processFile(e.target.files[0]);
    }
  };

  const processFile = (file) => {
    // Check if the file is an image
    if (!file.type.match('image.*')) {
      alert('Please select an image file');
      return;
    }
    
    // Check file size (limit to 5MB)
    if (file.size > 5 * 1024 * 1024) {
      alert('Image size should be less than 5MB');
      return;
    }
    
    setPreviewImage(URL.createObjectURL(file));
    onImageSelect(file);
  };

  const handleButtonClick = () => {
    fileInputRef.current.click();
  };

  return (
    <div className="image-upload-container">
      <div className="image-upload-header">
        <h3>Upload Image</h3>
        <button 
          className="close-button" 
          onClick={onCancel}
          aria-label="Close"
        >
          <FaTimes />
        </button>
      </div>
      
      <div 
        className={`drop-area ${dragActive ? 'active' : ''}`}
        onDragEnter={handleDrag}
        onDragOver={handleDrag}
        onDragLeave={handleDrag}
        onDrop={handleDrop}
      >
        {previewImage ? (
          <div className="preview-container">
            <img 
              src={previewImage} 
              alt="Preview" 
              className="image-preview" 
            />
          </div>
        ) : (
          <div className="upload-prompt">
            <FaUpload className="upload-icon" />
            <p>Drag & drop an image or click to browse</p>
            <input
              ref={fileInputRef}
              type="file"
              className="file-input"
              accept="image/*"
              onChange={handleFileChange}
            />
            <button 
              type="button"
              className="browse-button"
              onClick={handleButtonClick}
            >
              Browse Files
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default ImageUpload;