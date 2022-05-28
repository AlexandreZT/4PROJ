import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
// import { useNavigate } from 'react-router';
import Compta from './compta'
import Alternant from './alternant'
import Annuaire from './annuaire'
import Login from './login'
import '../style/master.css';

export default function Master() {
    // TODO : CHECK IS THERE IS CONNECTED USER:
    const isLoggedIn=true  // by default use this to simulate if user is connected
    // const navigate = useNavigate();
    const headerMenuItems = [
        {href: "/compta", title: "Compta"},
        {href: "/alternant", title: "Alternant"},
        {href: "/annuaire", title: "Annuaire"},
    ]

    if (isLoggedIn===true) {
        return (
            <Router>
                <div>
                    <div class="sidenav">
                        {headerMenuItems.map((values, index) =>
                            <li>
                                <Link style={{textDecoration: 'none'}} key={index} to={values.href}>{values.title}</Link>
                            </li>                             
                        )}
                    </div>
                    <div class="main-display">
                        <Routes>
                            <Route key="0" path="/compta" element={<Compta />} /> 
                            <Route key="1" path="/alternant" element={<Alternant />} />    
                            <Route key="2" path="/annuaire" element={<Annuaire />} />
                        </Routes>     
                    </div>                               
                </div>    
          </Router> 
        )
    }
    else {
        // navigate("/")
        return (
            <Login />
        )
    }
}