import React from 'react';
import {Link} from 'react-router-dom';
import { Line } from 'react-chartjs-2';

const data = {
  labels: ['January', 'February', 'March', 'April', 'May'],
  datasets: [
    {
      label: 'Recruitments',
      data: [3, 2, 5, 4, 7],
      borderColor: '#007bff',
      fill: false,
    },
  ],
};


function Dashboard() {
  return (
    <div className="dashboard">
    
      <h2>Welcome XXX,</h2>
      <Link to="/login">Go to Login</Link>
      <div className="stats-section">
        <div className="stats">
          <div className="stat-item">
            <p>Total Recruits from last month</p>
            <h3>1.3K</h3>
          </div>
          <div className="stat-item">
            <p>Jobs Created</p>
            <h3>107</h3>
          </div>
          <div className="stat-item">
            <p>On-Processing Candidates</p>
            <h3>2.7K</h3>
          </div>
        </div>
        <div className="chart">
          {/* Placeholder for chart */}
          <img src="chart-placeholder.png" alt="Chart" />
        </div>
      </div>

      <button className="create-job-btn">Create New JOB</button>

      <div className="job-details">
        <h3>Senior Software Developer</h3>
        <p>Location: Chennai</p>
        <p>Product Development</p>
        <p>Deadline: 29/09/2024</p>
        <p>Applied: 930</p>
      </div>
      
    </div>
    
  );
}

export default Dashboard;
