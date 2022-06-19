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
        if (token==="d79a1359d3da7dc28d04d1c1751b4201e94673005e015d89b0fc34cdd88a1587d4eec3a333e39237bfeb515642e933080103c1737e4463f38a9ecbe3c7f8f898") {
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
                    <div class="sidenav">
                        {headerMenuItems.map((values, index) =>
                            <li><Link key={index} to={values.href}>{values.title}</Link></li>                             
                        )}
                        <li><a href="#contact" onClick={disconnect}>Logout</a></li>
                    </div>
                    <div class="main-display">
                        <Routes>
                            <Route key="0" path="/"  element={<Directory />} /> 
                            <Route key="1" path="/absence"  element={<Absence />} /> 
                            <Route key="2" path="/comptability"  element={<Comptability />} /> 
                            <Route key="3" path="/contract" element={<Contract />} />    
                            <Route key="4" path="/directory" element={<Directory />} />
                            <Route key="5" path="/member" element={<Member />} />    
                            <Route key="6" path="/report" element={<Report />} />
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