import React, { Component } from "react";
// import { Link } from "react-router-dom";
import '../styles/Dashboard.css';

export default class Home extends Component {
  state = {
    dashboard_data: {},
    displayed_data: "users"
  }

  selectUsersDataForDashboard = this.selectUsersDataForDashboard.bind(this);
  selectStudentsDataForDashboard = this.selectStudentsDataForDashboard.bind(this);
  selectStaffsDataForDashboard = this.selectStaffsDataForDashboard.bind(this);
  selectTutorsDataForDashboard = this.selectTutorsDataForDashboard.bind(this);
  selectTeachersDataForDashboard = this.selectTeachersDataForDashboard.bind(this);
  loadData = this.loadData.bind(this);

  getUsersData() {
    if (this.state.dashboard_data) {       
        return Object.keys(this.state.dashboard_data).map( (id) => {
          return <tr>
            <td>{id}</td>
            <td>{this.state.dashboard_data[id]["email"]}</td>
            <td>{this.state.dashboard_data[id]["firstname"]}</td>
            <td>{this.state.dashboard_data[id]["lastname"]}</td>
            <td>{this.state.dashboard_data[id]["phone"]}</td>
            <td>{this.state.dashboard_data[id]["type"]}</td>
          </tr>;
      });
    } else {
        return <p>data is not available</p>;
    }
  }

  componentDidMount(){
    // TODO : si pas connecter alors redirection vers login sinon on lance bien le dashboard (home)
    // TODO : si connecter alors charger les données menu & users  
    this.loadData()
  }

  loadData() {
    var axios = require('axios');

    var config = {
      method: 'get',
      url: 'http://127.0.0.1:5000/'+this.state.displayed_data
    };
    
    axios(config)
    .then(response => this.setState({
      dashboard_data: response.data
    }))
    .catch(function (error) {
      console.log(error);
    });  
  }

  selectUsersDataForDashboard() {
    this.setState({ displayed_data: "users" }, () => {
      this.loadData()
    });
  }

  selectStudentsDataForDashboard() {
    this.setState({ displayed_data: "students" }, () => {
      this.loadData()
    });
  }

  selectStaffsDataForDashboard() {
    this.setState({ displayed_data: "staffs" }, () => {
      this.loadData()
    });
  }
  
  selectTutorsDataForDashboard() {
    this.setState({ displayed_data: "tutors" }, () => {
      this.loadData()
    });
  }

  selectTeachersDataForDashboard() {
    this.setState({ displayed_data: "teachers" }, () => {
      this.loadData()
    });
  }
  
  render() {    
    return (
      <div>      
        <div style={{textAlign: "center"}}>
          <button style={{width: "calc(100% / 5)"}} onClick={this.selectUsersDataForDashboard}>Users</button>
          <button style={{width: "calc(100% / 5)"}} onClick={this.selectStudentsDataForDashboard}>Students</button>
          <button style={{width: "calc(100% / 5)"}} onClick={this.selectStaffsDataForDashboard}>Staffs</button> 
          <button style={{width: "calc(100% / 5)"}} onClick={this.selectTutorsDataForDashboard}>Tutors</button>
          <button style={{width: "calc(100% / 5)"}} onClick={this.selectTeachersDataForDashboard}>Teachers</button> 
        </div>          
        <table style={{width: "100%"}} border={2} cellPadding={5}>
          <thead>
            {
              (this.state.displayed_data==="users" || 
              this.state.displayed_data==="students" ||
              this.state.displayed_data==="staffs" ||
              this.state.displayed_data==="tutors" ||
              this.state.displayed_data==="teachers") &&
              <tr>
                <td>id</td>
                <td>email</td>
                <td>firstname</td>
                <td>lastname</td>
                <td>phone</td>
                <td>type</td>
              </tr>          
            }            
          </thead>
          <tbody>
          { 
            (this.state.displayed_data==="users" || 
            this.state.displayed_data==="students" ||
            this.state.displayed_data==="staffs" ||
            this.state.displayed_data==="tutors" ||
            this.state.displayed_data==="teachers") &&
            this.getUsersData()
          }
          </tbody> 
        </table>
                
      </div>     
    );
  }
}