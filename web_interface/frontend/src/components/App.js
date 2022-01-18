import '../styles/App.css';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import logo from '../static/logo.png';
import Home from './Home';
import SignIn from './SignIn.js';

function App() {
  // const headerMenuItems = [
  //   {href: "/sign-in", title: "Sign in"},
  // ]

  return (    
    <Router>  
      <div className="App">
        <header className="App-header">        
          <nav style={{boxShadow: "0px 0px 5px 5px rgba(0, 0, 255, .2)"}}>            
            <Link to={"/"}>
              <img style={{padding:"10px"}} src={logo} width="180px" alt="PROJ"/>
            </Link>                     
            <ul>
            {/* {headerMenuItems.map((values, index) =>
              <li>
                <Link key={index} to={values.href}>{values.title}</Link>
              </li>                              
            )}           */}
            </ul>
          </nav>
          <Switch>
            <Route key="0" exact path="/" component={Home} />    
            <Route key="1" path="/sign-in" component={SignIn} />                 
          </Switch>      
        </header>
      </div>
    </Router>
  );
} 


export default App;