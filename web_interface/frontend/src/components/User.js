import React, { Component } from "react";
import '../styles/form.css';

export default class User extends Component {
    state = {
        users_data : {},
        displayed_action: "create",
        response: null
    }    

    selectCreateForUser = this.selectCreateForUser.bind(this);
    selectSearchForUser = this.selectSearchForUser.bind(this);
    selectUpdateForUser = this.selectUpdateForUser.bind(this);
    selectDeleteForUser = this.selectDeleteForUser.bind(this);

    searchUser = (e) => {
        e.preventDefault()
 
        var axios = require('axios');    
        
        if (e.target[0].value === "") {
            alert(`
            Enter Id !
            `)
        } else {
            axios({
                method: 'get',
                url: 'http://127.0.0.1:5000/user/'+e.target[0].value
            })
            .then(response  =>
                this.setState({
                    users_data: response.data
                })
            ) 
        }
                           
        axios({
            method: 'get',
            url: 'http://127.0.0.1:5000/user/'+e.target[0].value
        })
        .then(response  =>
            this.setState({
                users_data: response.data
            })
        )                           
    }

    createUser = (e) => {
        e.preventDefault()
        // TODO : ajout warning au front
        if (e.target[0].value === "" || e.target[0].value.length < 2 || // fn min 2 len
            e.target[1].value === "" || e.target[1].value.length < 2 || // ls min 2 len
            e.target[2].value === "" || e.target[2].value.length !== 10 || !isNaN(e.target[3].value) || // phone isNumeric with 10 digit
            e.target[3].value === "" ||  // email format already checked
            e.target[4].value === "" || e.target[4].value.length < 8 || // pass len 8 mini
            e.target[5].value === ""  ) { // type must be filled in            
            alert(`
            Firstname length 2+
            Lastname length 2+
            Phone must be in valid format
            Email must be in valid format
            Password lengh 8+
            `)
        } else {                
            fetch('http://127.0.0.1:5000/create-user', { // sign-up
                method: 'POST',
                headers:{
                    "Content-Type":"application/json"
                },
                body: JSON.stringify({
                    firstname : e.target[0].value.trim(),
                    lastname : e.target[1].value.trim(),
                    phone : e.target[2].value.trim(),
                    email : e.target[3].value.trim(),
                    password : e.target[4].value.trim(),
                    type : e.target[5].value.trim()
                }),
            }).then(async response => {
                this.setState({
                    response: response.status
                })
                }
                ).catch(error => {
                    this.setState({
                    response: 500
                })
            });
        }                     
    }

    updateUser = (e) => {
        e.preventDefault()
        // TODO : ajout warning au front
        if (e.target[0].value === "" || e.target[0].value.length < 2){ // id min 2 len
            alert(`
            Enter Id !
            `)
        } else {                
            fetch("http://127.0.0.1:5000/update-user-data-with-id", {
                method: 'PUT',
                headers:{
                    "Content-Type":"application/json"
                },
                body: JSON.stringify({
                    id : e.target[0].value,
                    firstname : e.target[1].value.trim(),
                    lastname : e.target[2].value.trim(),
                    phone : e.target[3].value.trim(),
                    email : e.target[4].value.trim(),
                    type : e.target[5].value.trim()
                }),
            }).then(async response => {
                    this.setState({
                        response: response.status
                    })
                }
            ).catch(error => {
                this.setState({
                    response: 500
                })
            });
        }                   
    }

    deleteUser = (e) => {
        e.preventDefault()
        // TODO : ajout warning au front
        if (e.target[0].value === "" || e.target[0].value.length < 2){ // id min 2 len
            alert(`
            Enter Id !
            `)
        } else {                
            fetch("http://127.0.0.1:5000/delete-user-with-id", {
                method: 'DELETE',
                headers:{
                    "Content-Type":"application/json"
                },
                body: JSON.stringify({
                    id : e.target[0].value.trim(),
                }),
            }).then(async response => {
                this.setState({
                    response: response.status
                })
            }
            ).catch(error => {
                this.setState({
                    response: 500
                })
            });
        }                   
    }

    selectCreateForUser () {
        this.setState({
            displayed_action: "create",
            response: null,

        })
    }

    selectSearchForUser () {
        this.setState({
            displayed_action: "search",
            response: null,
            users_data: {}
        })
    }
    
    selectUpdateForUser () {
        this.setState({
            displayed_action: "update",
            response: null,
            users_data: {}
        })
    }

    selectDeleteForUser() {
        this.setState({
            displayed_action: "delete",
            response: null,
            users_data: {}
        })
    }

    render() {
        return (
            <div>
                <div style={{textAlign: "center"}}>
                    <button style={{width: "calc(100% / 4)"}} onClick={this.selectCreateForUser}>Create user</button>
                    <button style={{width: "calc(100% / 4)"}} onClick={this.selectSearchForUser}>Search user</button>
                    <button style={{width: "calc(100% / 4)"}} onClick={this.selectUpdateForUser}>Update user</button>
                    <button style={{width: "calc(100% / 4)"}} onClick={this.selectDeleteForUser}>Delete user</button> 
                </div>
                <br/>
                

                {this.state.displayed_action === "create" ?
                           
                <div className="auth-inner" >
                    <form onSubmit={this.createUser}>
                        <h3>Create user</h3>
                        <div className="form-group">
                            <label>Firstname</label><br/>
                            <input type="text" className="form-control" placeholder="Enter Firstname" />
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Lastname</label><br/>
                            <input type="text" className="form-control" placeholder="Enter Lastname" />
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Phone</label><br/>
                            <input type="text" className="form-control" placeholder="Enter Phone" />
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Email</label><br/>
                            <input type="email" className="form-control" placeholder="Enter Email" />
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Password</label><br/>
                            <input type="password" className="form-control" placeholder="Enter Password" />
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Role</label><br/>
                            <select name="type">                                
                                <option value="students">Students</option>
                                <option value="staffs">Staffs</option>
                                <option value="tutors">Tutors</option>
                                <option value="teachers">Teachers</option>
                            </select>
                        </div>
                        <br/>
                        <button type="submit" className="btn btn-primary btn-block">Create</button>
                        {   
                            this.state.response===null?
                            <p></p>:
                            this.state.response===200?
                            <p style={{color:"green"}}>User created !</p>:
                            this.state.response===500 &&
                            <p style={{color:"red"}}>Something went wrong !</p>
                        }
                    </form>
                </div>: this.state.displayed_action === "search" ?
                <div className="auth-inner">
                    <form onSubmit={this.searchUser}>                    
                        <h3>Search user</h3><br/>
                        <div className="form-group">
                            <label>User Id*</label><br/>
                            <input type="text" placeholder="Search user by id"/>                            
                        </div>
                        <br/>
                        <button type="submit" className="btn btn-primary btn-block">Search</button>                                                         
                    </form>

                    {
                        this.state.users_data != null ?
                        Object.keys(this.state.users_data).map((key) => (
                            <p>{key} : {this.state.users_data[key]}</p>                                      
                        )) : 
                        <p style={{color:"red"}}>Something went wrong !</p>
                    }
                 </div>
                : this.state.displayed_action === "update" ?
                <div className="auth-inner">
                    <form onSubmit={this.updateUser}>
                        <h3>Update user</h3>
                        <div className="form-group">
                            <label>User Id*</label><br/>
                            <input type="text" className="form-control" placeholder="Enter Id" />
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Firstname</label><br/>
                            <input type="text" className="form-control" placeholder="New Firstname" />
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Lastname</label><br/>
                            <input type="text" className="form-control" placeholder="New Lastname" />
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Phone</label><br/>
                            <input type="text" className="form-control" placeholder="New Phone" />
                        </div>
                        <br/>
                        <div className="form-group">
                            <label>Email</label><br/>
                            <input type="email" className="form-control" placeholder="New Email" />
                        </div>      
                        <br/>
                        <div className="form-group">
                            <label>Role</label><br/>
                            <select name="type">
                                <option value="">New Role</option>
                                <option value="students">Students</option>
                                <option value="staffs">Staffs</option>
                                <option value="tutors">Tutors</option>
                                <option value="teachers">Teachers</option>
                            </select>
                        </div>
                        <br/>
                        <button type="submit" className="btn btn-primary btn-block">Update</button>
                        {   
                            this.state.response===null?
                            <p></p>:
                            this.state.response===200?
                            <p style={{color:"green"}}>User updated !</p>:
                            this.state.response===500 &&
                            <p style={{color:"red"}}>Something went wrong !</p>
                        }
                    </form>
                </div>
                : this.state.displayed_action === "delete" &&
                <div className="auth-inner">
                    <form onSubmit={this.deleteUser}>                    
                        <h3>Delete user</h3><br/>
                        <div className="form-group">
                            <label>User Id*</label><br/>
                            <input type="text" placeholder="Delete user by id"/>                            
                        </div>
                        <br/>
                        <button type="submit" className="btn btn-primary btn-block">Delete</button>
                        {   
                            this.state.response===null?
                            <p></p>:
                            this.state.response===200?
                            <p style={{color:"green"}}>User deleted !</p>:
                            this.state.response===500 &&
                            <p style={{color:"red"}}>Something went wrong !</p>
                        }                                                    
                    </form>                    
                 </div>
                }                                    
            </div>
        );
    }
}