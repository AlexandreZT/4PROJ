import React, { useState, useEffect } from 'react';


export default function Member() {
    // TODO : improve by giving a list of input & options
    const display_student_form = () => {
        return (
            <div className="auth-inner">
                <form onSubmit>
                    <h3>Create Student</h3>
                    <div className="form-group">
                        <label>First name*</label><br/>
                        <input type="text" className="form-control" placeholder="Enter First Name" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Last name*</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Last Name" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Email</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Email" />
                    </div>
                    <br/>                           
                    <div className="form-group">
                        <label>Campus</label><br/>
                        <select name="type">
                        <option value="distanciel">Distanciel</option>
                        <option value="paris">Paris</option>
                        <option value="caen">Caen</option>
                        <option value="lille">Lille</option>
                        <option value="lyon">Lyon</option>
                        <option value="tours">Tours</option>
                        </select>
                    </div>
                    <br/>
                    <div className="form-group">
                        <label for="start">Birth date</label><br/>
                        <input type="date" id="start" name="trip-start" min="1920-01-01"/>
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Address</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Address" />
                    </div>
                    <br/>                
                    <div className="form-group">
                        <label>Gender</label><br/>
                        <select name="type">
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        </select>
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Region</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Region" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Level</label><br/>
                        <select name="level">
                            <option value="beng1">B.Eng.1</option>
                            <option value="beng2">B.Eng.2</option>
                            <option value="beng3">B.Eng.3</option>
                            <option value="meng1">M.Eng.1</option>
                            <option value="meng2">M.Eng.2</option>
                        </select>
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Speciality</label><br/>
                        <select name="spe">
                            <option value="beng">B.Eng</option>
                            <option value="ia">Intelligence Artificielle</option>
                            <option value="srs">Systemes Reseaux et securité</option>
                            <option value="data">Data Engineering</option>
                        </select>
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Alternance</label><br/>
                        <select name="cp">
                            <option value="no">No</option>
                            <option value="yes">Yes</option>                            
                        </select>
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Previous level</label><br/>
                        <select name="previous-level">
                            <option value="bac">BAC</option>
                            <option value="beng1">BTS</option>
                            <option value="beng2">DUT</option>
                            <option value="beng3">Licence</option>
                            <option value="meng1">Master</option>
                            <option value="beng1">B.Eng.1</option>
                            <option value="beng2">B.Eng.2</option>
                            <option value="beng3">B.Eng.3</option>
                            <option value="meng1">M.Eng.1</option>
                            <option value="meng2">M.Eng.2</option>
                        </select>
                    </div>
                    <br/>
                    <div className="form-group">
                    <label>Age of entry</label><br/>
                        <input type="number" min="10" max="100"></input>
                    </div>
                    <br/>
                    <button type="submit" className="btn btn-primary btn-block">Create</button>
                    {/* {   
                        this.state.response===null?
                        <p></p>:
                        this.state.response===200?
                        <p style={{color:"green"}}>User created !</p>:
                        this.state.response===500 &&
                        <p style={{color:"red"}}>Something went wrong !</p>
                    } */}
                </form>
            </div>
        )       
        // age_of_entry=None,

    }
    
    const display_staff_form = () => {
        return (
            <div className="auth-inner">
                <form onSubmit>
                    <h3>Create Staff</h3>
                    <div className="form-group">
                        <label>First name*</label><br/>
                        <input type="text" className="form-control" placeholder="Enter First Name" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Last name*</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Last Name" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Email</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Email" />
                    </div>
                    <br/> 
                    <div className="form-group">
                        <label>Campus</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Campus" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Phone</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Phone" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Role</label><br/>
                        <select name="type">
                        <option value="coordonator">Coordinateur</option>
                        <option value="full-professor">Full Professor</option>
                        <option value="academic-director">Directeur academique</option>
                        </select>
                    </div>
                    <br/>
                    <button type="submit" className="btn btn-primary btn-block">Create</button>
                    {/* {   
                        this.state.response===null?
                        <p></p>:
                        this.state.response===200?
                        <p style={{color:"green"}}>User created !</p>:
                        this.state.response===500 &&
                        <p style={{color:"red"}}>Something went wrong !</p>
                    } */}
                </form>
            </div>
        )
    }

    const display_tutor_form = () => {
        return (
            <div className="auth-inner">
                <form onSubmit>
                    <h3>Create Tutor</h3>
                    <div className="form-group">
                        <label>First name*</label><br/>
                        <input type="text" className="form-control" placeholder="Enter First Name" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Last name*</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Last Name" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Email</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Email" />
                    </div>
                    <br/> 
                    <div className="form-group">
                        <label>Phone</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Phone" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Gender</label><br/>
                        <select name="type">
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        </select>
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Enterprise Name</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Enterprise Name" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Enterprise Location</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Enterprise Location" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Job</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Job" />
                    </div>
                    <br/>
                    <button type="submit" className="btn btn-primary btn-block">Create</button>
                    {/* {   
                        this.state.response===null?
                        <p></p>:
                        this.state.response===200?
                        <p style={{color:"green"}}>User created !</p>:
                        this.state.response===500 &&
                        <p style={{color:"red"}}>Something went wrong !</p>
                    } */}
                </form>
            </div>
        )
    }

    const display_teacher_form = () => {
        return (
            <div className="auth-inner">
                <form onSubmit>
                    <h3>Create Teacher</h3>
                    <div className="form-group">
                        <label>First name*</label><br/>
                        <input type="text" className="form-control" placeholder="Enter First Name" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Last name*</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Last Name" />
                    </div>
                    <br/>
                    <div className="form-group">
                        <label>Email*</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Email" />
                    </div>
                    <br/> 
                    <div className="form-group">
                        <label>Phone</label><br/>
                        <input type="text" className="form-control" placeholder="Enter Phone" />
                    </div>
                    <br/>
                    <button type="submit" className="btn btn-primary btn-block">Create</button>
                    {/* {   
                        this.state.response===null?
                        <p></p>:
                        this.state.response===200?
                        <p style={{color:"green"}}>User created !</p>:
                        this.state.response===500 &&
                        <p style={{color:"red"}}>Something went wrong !</p>
                    } */}
                </form>
            </div>
        )
    }

    const  [state, setState] = useState({displayed_form: display_student_form(), chosen_user: "student"});

    function changeUserForm(e) {
        let {name, value} = e.target;
        if (value === "student"){
            setState({...state, chosen_user: value, displayed_form: display_student_form()});
        } else if (value === "staff") {
            setState({...state, chosen_user: value, displayed_form: display_staff_form()});
        } else if (value === "tutor") {
            setState({...state, chosen_user: value, displayed_form: display_tutor_form()});
        } else if (value === "teacher") {
            setState({...state, chosen_user: value, displayed_form: display_teacher_form()});
        }
    }

    // this hook will get called everytime when state has changed
     useEffect (() => { 
        // perform some action which will get fired everytime when state gets updated
           console.log('Current state:', state)
        }, [state]
    )

    return (
        <div>
            <label>Select Form:&nbsp;</label>
            
            <select onChange={changeUserForm}>
                <option value="student">student</option>
                <option value="staff">staff</option>
                <option value="tutor">tutor</option>
                <option value="teacher">teacher</option>
            </select>
            {state.displayed_form}
        </div>
    )
}