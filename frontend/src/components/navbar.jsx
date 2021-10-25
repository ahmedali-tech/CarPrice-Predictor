import React, { Component } from "react";
import "./navbar.css";

class Navbar extends React.Component {
  render() {
    return (
      <>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
          <div class="container-fluid">
            <h2 className=" offset-lg-5 heading">CAR PRICES</h2>
          </div>
        </nav>
      </>
    );
  }
}

export default Navbar;
