import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
// import { useNavigate } from 'react-router';
import React, { useState, useEffect } from 'react';
import Absence from './absence'
import Comptability from './comptability'
import Contract from './contract'
import Directory from './directory'
import Login from './login'
import Member from './member'
import Report from './report'

import '../style/master.css';

export default function Master() {
    // TODO : CHECK IS THERE IS CONNECTED USER:
    const [isOnline, setIsOnline] = useState(false); // by default use this to simulate if user is connected
    // let  navigate = useNavigate(); // redirect => white screen
    const headerMenuItems = [
        {href: "/absence", title: "Absence"},
        {href: "/comptability", title: "Comptability"},
        {href: "/contract", title: "Contract"},
        {href: "/directory", title: "Directory"},
        {href: "/member", title: "Member"},
        {href: "/report", title: "Report"}
    ]

    useEffect(() => {
        // check is there is a token stored
        let token = localStorage.getItem('localId')
        if (token==="iamastrangetokenxdplzdontjudgemewhyareyoulaughing") {
            setIsOnline(true)
        }
        else {
            setIsOnline(false)
        }
    },  [isOnline]);

    function disconnect () {
        localStorage.removeItem("localId"); // localStorage.clear();
        window.location.reload(false);
    }

    if (isOnline) {
        return (
            <Router>
                <div>
                    <header>
                        <nav>  
                            <ul>
                            <li> <a href="#"> Profile </a>  
                            </li>  
                            <li>  
                            <a href="#"> Settings </a>  
                            </li>
                            <li style={{paddingRight: 0}}>  
                                <a href="#" onClick={disconnect}> Logout </a>  
                            </li>   
                            </ul>  
                        </nav>  
                    </header>
                    <div class="sidenav">
                        {headerMenuItems.map((values, index) =>
                            <li><Link key={index} to={values.href}>{values.title}</Link></li>                             
                        )}
                    </div>
                    <div class="main-display">
                        <Routes>
                            <Route key="0" path="/absence"  element={<Absence />} /> 
                            <Route key="1" path="/comptability"  element={<Comptability />} /> 
                            <Route key="2" path="/contract" element={<Contract />} />    
                            <Route key="3" path="/directory" element={<Directory />} />
                            <Route key="4" path="/member" element={<Member />} />    
                            <Route key="5" path="/report" element={<Report />} />
                        </Routes>     
                    </div>                               
                </div>    
          </Router> 
        )
    }
    else {
        
        // navigate("/") // redirect me there plz
        return (
            <Login />
        )
    }
}