// src/services/api.js
import axios from 'axios';

// Configure the base URL of your FastAPI backend
const API_URL = 'http://127.0.0.1:8000';

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
});

export const sendMessage = async (message, imageFile = null) => {
  try {
    // Create FormData for the request
    const formData = new FormData();
    
    // Add message if provided
    if (message) {
      formData.append('message', message);
    }
    
    // Add image if provided
    if (imageFile) {
      formData.append('image', imageFile);
    }
    
    // Make the API call to the chat endpoint
    const response = await axios.post(`${API_URL}/chat`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        // 'Origin': 'http://localhost:3000',  // Explicitly set frontend origin
      },
      // withCredentials: true,  // If your API requires authentication
    });
    
    
    // Return the response from the backend
    if (response.data.response) {
      return { message: response.data.response };
    } else if (response.data.error) {
      throw new Error(response.data.error);
    }
    
    return response.data;
  } catch (error) {
    console.error('Error in chat request:', error);
    throw error;
  }
};

// No need for a separate uploadImage function since we handle images in sendMessage