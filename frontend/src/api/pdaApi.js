import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:5000/api";

export async function getSamples() {
  const response = await axios.get(`${API_BASE_URL}/samples`);
  return response.data;
}

export async function simulatePDA(pda, inputString) {
  const response = await axios.post(`${API_BASE_URL}/simulate`, {
    pda,
    input_string: inputString,
  });
  return response.data;
}

export async function renderGraph(pda) {
  const response = await axios.post(`${API_BASE_URL}/render-graph`, {
    pda,
  });
  return response.data;
}

export async function convertToCFG(pda) {
  const response = await axios.post(`${API_BASE_URL}/cfg-convert`, {
    pda,
  });
  return response.data;
}