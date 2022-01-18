import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import '../styles/Dashboard.css';
import Dasboard from './Dashboard'
import Menu from './Menu'
import Sells from './Sells'
import Stocks from './Stocks'
import User from './User'
import Map from './Map'

export default class Home extends Component {
  
  headerMenuItems = [
      {href: "/dashboard", title: "Dashoard"},
      {href: "/user", title: "User"},
      {href: "/menu", title: "Menu"},
      {href: "/map", title: "Map"},        
      {href: "/sells", title: "Sells"},
      {href: "/stocks", title: "Stocks"},        
  ]

  componentDidMount() {
    var axios = require('axios'); 

    axios({
        method: 'get',
        url: 'http://127.0.0.1:5000/data'
    })       
  }

  render() {
    return (      
        <Router>  
            <div>    
                {this.headerMenuItems.map((values, index) =>
                    <li style={{width: "calc(100% / 6)", display: "inline", padding:"7%"}}>
                        <Link style={{textDecoration: 'none'}} key={index} to={values.href}>{values.title}</Link>
                    </li>                             
                )}
                
                <Switch>
                    <Route key="10" path="/dashboard" component={Dasboard} /> 
                    <Route key="11" path="/menu" component={Menu} />    
                    <Route key="12" path="/sells" component={Sells} />
                    <Route key="13" path="/stocks" component={Stocks} /> 
                    <Route key="14" path="/user" component={User} />    
                    <Route key="15" path="/map" component={Map} />            
                </Switch>                                    
        </div>    
      </Router>   
    );
  }
}