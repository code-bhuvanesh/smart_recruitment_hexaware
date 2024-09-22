import React from 'react';

function Sidebar() {
  return (
    <div className="sidebar">
      <h3>Applicant login -HR</h3>
      <ul>
        <li>Dashboard</li>
        <li>Job Creation</li>
        <li>Applications</li>
        <li>Forms</li>
      </ul>
      <button className="logout-btn">Log Out</button>
    </div>
  );
}

export default Sidebar;
