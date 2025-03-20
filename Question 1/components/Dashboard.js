import React, { useState } from "react";
import "./Dashboard.css"; // Ensure this file exists

const Dashboard = () => {
  const [apiEndpoint, setApiEndpoint] = useState("/users");
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const fetchData = () => {
    fetch(apiEndpoint)
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        setError(null);
      })
      .catch((err) => {
        setError("Error fetching data. Check API endpoint.");
        setData(null);
        console.error("Fetch error:", err);
      });
  };

  return (
    <div className="dashboard">
      <h1 className="title">⚡ Social Media API Handling Dashboard</h1>

      {/* API Input Field */}
      <div className="api-input">
        <input
          type="text"
          value={apiEndpoint}
          onChange={(e) => setApiEndpoint(e.target.value)}
          placeholder="Enter API Endpoint (e.g., /users, /top_users, /posts?type=popular)"
        />
        <button onClick={fetchData}>Fetch Data</button>
      </div>

      {/* Display Results */}
      {error && <p className="error">{error}</p>}
      {data && (
        <div className="result">
          <h2>💾 API Response:</h2>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default Dashboard;
