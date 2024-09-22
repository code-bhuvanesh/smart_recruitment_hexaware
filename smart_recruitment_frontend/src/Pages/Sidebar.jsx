import React from 'react';
import { Link } from 'react-router-dom';

function Sidebar() {
  return (
    <div className="sidebar">
      <h3>Applicant login - HR</h3>
      <ul>
        <li>
          <Link to="/dashboard">Dashboard</Link>
        </li>
        <li>
          <Link to="/job-creation">Job Creation</Link>
        </li>
        <li>
          <Link to="/applications">Applications</Link>
        </li>
        <li>
          <Link to="/forms">Forms</Link>
        </li>
      </ul>
      <button className="logout-btn">Log Out</button>
    </div>
  );
}

export default Sidebar;
