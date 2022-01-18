import React, { Component } from "react";
// import { Link } from "react-router-dom";
import '../styles/Dashboard.css';

export default class Home extends Component {
  state = {
    dashboard_data: {},
    displayed_data: "users"
  }

  selectUsersDataForDashboard = this.selectUsersDataForDashboard.bind(this);
  selectCooksDataForDashboard = this.selectCooksDataForDashboard.bind(this);
  selectCustomersDataForDashboard = this.selectCustomersDataForDashboard.bind(this);
  selectWaitersDataForDashboard = this.selectWaitersDataForDashboard.bind(this);
  selectBarmenDataForDashboard = this.selectBarmenDataForDashboard.bind(this);
  selectMenuDataForDashboard = this.selectMenuDataForDashboard.bind(this);
  selectDrinksDataForDashboard = this.selectDrinksDataForDashboard.bind(this);
  selectFoodsDataForDashboard = this.selectFoodsDataForDashboard.bind(this);
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

  getMenuData() {
    if (this.state.dashboard_data) {
        return Object.keys(this.state.dashboard_data).map( (id) => {
          return <tr>
            <td>{id}</td>
            <td>{this.state.dashboard_data[id]["name"]}</td>
            <td>{this.state.dashboard_data[id]["description"]}</td>
            <td>{this.state.dashboard_data[id]["price"]}</td>
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

  selectCooksDataForDashboard() {
    this.setState({ displayed_data: "cooks" }, () => {
      this.loadData()
    });
  }

  selectCustomersDataForDashboard() {
    this.setState({ displayed_data: "customers" }, () => {
      this.loadData()
    });
  }
  
  selectWaitersDataForDashboard() {
    this.setState({ displayed_data: "waiters" }, () => {
      this.loadData()
    });
  }

  selectBarmenDataForDashboard() {
    this.setState({ displayed_data: "barmen" }, () => {
      this.loadData()
    });
  }

  selectMenuDataForDashboard() {
    this.setState({ displayed_data: "menu" }, () => {
      this.loadData()
    });
  }
  
  selectDrinksDataForDashboard() {
    this.setState({ displayed_data: "drinks" }, () => {
      this.loadData()
    });
  }

  selectFoodsDataForDashboard() {
    this.setState({ displayed_data: "foods" }, () => {
      this.loadData()
    });
  }
  
  render() {    
    return (
      <div>      
        <div style={{textAlign: "center"}}>
          <button style={{width: "calc(100% / 8)"}} onClick={this.selectUsersDataForDashboard}>Users</button>
          <button style={{width: "calc(100% / 8)"}} onClick={this.selectCooksDataForDashboard}>Cooks</button>
          <button style={{width: "calc(100% / 8)"}} onClick={this.selectCustomersDataForDashboard}>Customers</button> 
          <button style={{width: "calc(100% / 8)"}} onClick={this.selectWaitersDataForDashboard}>Waiters</button>
          <button style={{width: "calc(100% / 8)"}} onClick={this.selectBarmenDataForDashboard}>Barmen</button> 
          <button style={{width: "calc(100% / 8)"}} onClick={this.selectMenuDataForDashboard}>Menu</button>
          <button style={{width: "calc(100% / 8)"}} onClick={this.selectDrinksDataForDashboard}>Drinks</button>
          <button style={{width: "calc(100% / 8)"}} onClick={this.selectFoodsDataForDashboard}>Foods</button> 
        </div>
          
        <table style={{width: "100%"}} border={2} cellPadding={5}>
          <thead>
            {
              (this.state.displayed_data==="users" || 
              this.state.displayed_data==="cooks" ||
              this.state.displayed_data==="barmen" ||
              this.state.displayed_data==="waiters" ||
              this.state.displayed_data==="customers") ?
              <tr>
                <td>id</td>
                <td>email</td>
                <td>firstname</td>
                <td>lastname</td>
                <td>phone</td>
                <td>type</td>
              </tr> :
              (this.state.displayed_data==="menu" || 
              this.state.displayed_data==="foods" ||
              this.state.displayed_data==="drinks") &&
              <tr>
                <td>id</td>                
                <td>name</td>
                <td>description</td>
                <td>price</td>
                <td>type</td>
              </tr>              
            }            
          </thead>
          <tbody>
          { 
            (this.state.displayed_data==="users" || 
            this.state.displayed_data==="cooks" ||
            this.state.displayed_data==="barmen" ||
            this.state.displayed_data==="waiters" ||
            this.state.displayed_data==="customers") ?
            this.getUsersData():
            (this.state.displayed_data==="menu" || 
            this.state.displayed_data==="foods" ||
            this.state.displayed_data==="drinks") &&
            this.getMenuData()
          }
          </tbody> 
        </table>
                
      </div>     
    );
  }
}