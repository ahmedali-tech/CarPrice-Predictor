import React, { Component } from "react";
import "./jumbo.css";

class Jumbotron extends React.Component {
  style = {
    height: window.innerHeight + 100,
    width: window.innerWidth - 50,
  };
  render() {
    return (
      <>
        <div className="jumbotron w-100" style={this.style}>
          <div className=" formstyle">
            <div className="innerform">
              <form action="/" method="POST">
                <div class="form-group">
                  <h4 className="selectlabel">Car Name</h4>
                  <select
                    class="form-control"
                    id="exampleFormControlSelect1"
                    name="car"
                  >
                    <option>ritz</option>
                    <option>sx4</option>
                    <option>Activa 3g</option>
                    <option>Activa 4g</option>
                    <option>Bajaj Avenger 150</option>
                    <option>s cross</option>
                    <option>verna</option>
                    <option>vitara brezza </option>
                    <option>wagon r</option>
                    <option>xcent</option>
                  </select>
                </div>
                <div class="form-group">
                  <h4 className="selectlabel">Transmission type</h4>
                  <select
                    class="form-control"
                    id="exampleFormControlSelect1"
                    name="transmission"
                  >
                    <option>Automatic</option>
                    <option>Manual</option>
                  </select>
                </div>
                <div class="form-group">
                  <h4 className="selectlabel">Fuel Type</h4>
                  <select
                    class="form-control"
                    id="exampleFormControlSelect1"
                    name="fuel"
                  >
                    <option>Petrol</option>
                    <option>Diesel</option>
                  </select>
                </div>
                <div class="form-group">
                  <h4 className="selectlabel">Present Owner</h4>
                  <select
                    class="form-control"
                    id="exampleFormControlSelect1"
                    name="owner"
                  >
                    <option>Yes</option>
                    <option>No</option>
                  </select>
                </div>
                <div class="form-group">
                  <h4 className="selectlabel">Selling yourself?</h4>
                  <select
                    class="form-control"
                    id="exampleFormControlSelect1"
                    name="seller"
                  >
                    <option>Yes</option>
                    <option>No</option>
                  </select>
                </div>
                <h4 className="selectlabel">Year</h4>
                <input type="number" className="inputplace" name="year" />
                <h4 className="selectlabel">Estimated Price in Lakhs</h4>
                <input type="number" className="inputplace" name="price" />
                <h4 className="selectlabel">Km Driven</h4>
                <input type="number" className="inputplace" name="kms" />

                <button type="submit" class="btn btn-primary btn-block ">
                  Submit
                </button>
              </form>
              <h1 className="answer"> Price={window.predict}</h1>
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default Jumbotron;
