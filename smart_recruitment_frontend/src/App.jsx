import React from 'react';
import Sidebar from './Pages/Sidebar';
import Dashboard from './Pages/Dashboard';
import LoginPage from './Pages/LoginPage';
import './App.css'; // Include your custom styles
import Register from './Pages/Register';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    // <div className="app">
    //   {/* <Sidebar />
    //   <Dashboard /> */}
   
    // </div>
    <Router>
      <Routes>
        <Route path='/'element={<Dashboard/>}/>
        <Route path="/login" element={<LoginPage/>}/>
        <Route path="/register" element={<Register/>}/>
      </Routes>
    </Router>
  );
}

export default App;
