import React from 'react';
import './LoginPage.css';
import {Link} from 'react-router-dom';

const LoginPage = () => {
  return (
    <div className="login-container">
      {/* Left section for background image or pattern */}
      <div className="login-bg">
        <h1 className="bg-text">Applicant Login</h1>
      </div>

      {/* Right section for the login form */}
      <div className="login-form-container">
        <form className="login-form">
          <h2>Login</h2>
          <div className="form-group">
            <label htmlFor="username">Username/Email</label>
            <input
              type="text"
              id="username"
              name="username"
              placeholder="Enter your username or email"
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              placeholder="Enter your password"
              required
            />
          </div>
          <div className="form-group">
            <input type="checkbox" id="rememberMe" name="rememberMe" />
            <label htmlFor="rememberMe">Remember me</label>
          </div>
          <div className="form-group">
            <button type="submit" id="loginBtn">Login</button>
          </div>
          <div className="form-links">
            <a href="/forgot-password">Forgot password?</a>
            <br />
            <Link to="/register">Go to Register</Link>
           
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
