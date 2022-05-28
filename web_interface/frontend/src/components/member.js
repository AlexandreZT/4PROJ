import React, { useState, useEffect } from 'react';
// TODO : if user_type is staff, he can add users

export default function Member() {
    // create which kind of user : student, staff, tutor or teacher ?
    // let chosen_user = "student" // default value
    // let displayed_form = null
    const  [state, setState] = useState({displayed_form: null, chosen_user: null});

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

    let display_student_form = () => {
        return (
            <div><p>ITS ME STUUDYY</p></div>
        )
    }
    
    let display_staff_form = () => {
        return (
            <div><p>ITS ME STAAFYY</p></div>
        )
    }

    function display_tutor_form(){
        return (
            <div><p>ITS ME TUUTTYY</p></div>
        )
    }

    function display_teacher_form(){
        return (
            <div><p>ITS ME TEAACHYY</p></div>
        )
    }

    
    // function select_displayed_form(){
    //     console.log("chosen_user", chosen_user)
    
    
    return (
        <div>
            <select onChange={changeUserForm}>
                <option value="">User type</option>
                <option value="student">student</option>
                <option value="staff">staff</option>
                <option value="tutor">tutor</option>
                <option value="teacher">teacher</option>
            </select>
            {state.displayed_form}
        </div>
    )
    
    // return (
    //     <div className="auth-inner">
    //         <form onSubmit>
    //             <h3>Create User</h3>
    //             <div className="form-group">
    //                 <label>First name</label><br/>
    //                 <input type="text" className="form-control" placeholder="Enter Name" />
    //             </div>
    //             <br/>
    //             <div className="form-group">
    //                 <label>Last name</label><br/>
    //                 <input type="text" className="form-control" placeholder="Enter Description" />
    //             </div>
    //             <br/>
    //             <div className="form-group">
    //                 <label>Price</label><br/>
    //                 <input type="text" className="form-control" placeholder="Enter Price" />
    //             </div>
    //             <br/>                           
    //             <div className="form-group">
    //                 <label>Category</label><br/>
    //                 <select name="type">
    //                 <option value="">Category</option>
    //                     <option value="side">Side</option>
    //                     <option value="pizza">Pizza</option>
    //                     <option value="burger">Burger</option>
    //                     <option value="salad">Salad</option>
    //                     <option value="cake">Cake</option>
    //                     <option value="cold drink">Cold drink</option>
    //                     <option value="hot drink">Hot drink</option>
    //                 </select>
    //             </div>
    //             <br/>
    //             <button type="submit" className="btn btn-primary btn-block">Create</button>
    //             {   
    //             this.state.response===null?
    //             <p></p>:
    //             this.state.response===200?
    //             <p style={{color:"green"}}>Product created !</p>:
    //             this.state.response===500 &&
    //             <p style={{color:"red"}}>Something went wrong !</p>
    //         }
    //         </form>
    //     </div>
    // )
}