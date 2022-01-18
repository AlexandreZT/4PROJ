import React, { Component } from 'react';
import '../styles/form.css';

export default class SignIn extends Component {

    constructor(props) {
        super(props);
        this.state = {            
        }
    }

    handleSubmit = (e) => {
        e.preventDefault()
        if (e.target[0].value === "" ||  // email format already checked
            e.target[1].value === "" || e.target[1].value.length < 8) { // len 8 mini
            alert(`
            Email must be in valid format
            Password lengh 8+
            `)
        } else {
            fetch('http://localhost:5000/sign-in', {
                method: 'POST',
                headers:{
                    "Content-Type":"application/json"
                },
                body: JSON.stringify({
                    email : e.target[0].value.trim(),
                    password : e.target[1].value.trim()
                }),
            }).then(response => {
                console.log(response)
                if (response === 200) {
                    this.props.history.push("/");
                    return
                }
            }) // .catch(err => console.log(err)); 
        }
    }

    render() {
        return (
            <div className="auth-wrapper">
                <div className="auth-inner">
                    <form onSubmit={this.handleSubmit}>
                        <h3>Sign In</h3>
                        <div className="form-group">
                            <label>Email</label><br/>
                            <input type="email" className="form-control" placeholder="Enter email"/>
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Password</label><br/>
                            <input type="password" className="form-control" placeholder="Enter password"/>
                        </div>
                        <br/>
                        <div className="form-group">
                            <div className="custom-control custom-checkbox">
                                <input type="checkbox" className="custom-control-input" id="customCheck1" />
                                <label className="custom-control-label" htmlFor="customCheck1">Remember me</label>
                            </div>
                        </div>
                        <br/>
                        <button type="submit" className="btn btn-primary btn-block">Sign In</button>
                        <p className="forgot-password text-right">
                            Forgot <a href="/sign-in#">password?</a>
                        </p>
                    </form>
                </div>
            </div>
        );
    }
}

