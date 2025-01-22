const BASE_URL = "http://127.0.0.1:8000";

export const getHelloMessage = async () => {
    const response = await fetch(`${BASE_URL}/api/hello`);
    return response.json();
};
