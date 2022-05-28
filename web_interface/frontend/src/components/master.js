import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
// import { useNavigate } from 'react-router';
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
    const isLoggedIn=true  // by default use this to simulate if user is connected
    // const navigate = useNavigate();
    const headerMenuItems = [
        {href: "/absence", title: "Absence"},
        {href: "/comptability", title: "Comptability"},
        {href: "/contract", title: "Contract"},
        {href: "/directory", title: "Directory"},
        {href: "/member", title: "Member"},
        {href: "/report", title: "Report"}
    ]

    if (isLoggedIn===true) {
        return (
            <Router>
                <div>
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
        // navigate("/") # redirect me there plz
        return (
            <Login />
        )
    }
}