import React, { useEffect, useState } from "react";
import { getHelloMessage } from "./api";

function App() {
    const [message, setMessage] = useState("");

    useEffect(() => {
        getHelloMessage().then((data) => setMessage(data.message));
    }, []);

    return (
        <div>
            <h1>React + FastAPI</h1>
            <p>{message}</p>
        </div>
    );
}

export default App;

