// src/services/api.js
import axios from 'axios';

// Configure the base URL of your FastAPI backend
const API_URL ="https://vesta-x7zr.onrender.com";
const API_URL_2 = "http://127.0.0.1/8000"

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
});

export const sendMessage = async (message, imageFile = null, searchRequired = false) => {
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
    
    // Add search_required flag
    formData.append('search_required', searchRequired);
    
    // Make the API call to the chat endpoint
    const response = await axios.post(`${API_URL}/chat`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    
    // Return the response from the backend
    console.log(response.data)
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