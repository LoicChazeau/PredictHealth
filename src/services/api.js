import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const getData = async () => {
    const response = await axios.get(`${API_URL}/data`);
    return response.data;
};

export const getPrediction = async (date) => {
    const response = await axios.get(`${API_URL}/predict/${date}`);
    return response.data;
};
