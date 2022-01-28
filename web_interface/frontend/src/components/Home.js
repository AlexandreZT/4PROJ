import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import '../styles/Dashboard.css';
import Dasboard from './Dashboard'
import User from './User'


export default class Home extends Component {
  
  headerMenuItems = [
      {href: "/dashboard", title: "Dashoard"},
      {href: "/user", title: "User"},       
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
                    <li style={{width: "calc(100% / 2)", display: "inline", padding:"7%"}}>
                        <Link style={{textDecoration: 'none'}} key={index} to={values.href}>{values.title}</Link>
                    </li>                             
                )}
                
                <Switch>
                    <Route key="10" path="/dashboard" component={Dasboard} /> 
                    <Route key="14" path="/user" component={User} />    
                </Switch>                                    
        </div>    
      </Router>   
    );
  }
}