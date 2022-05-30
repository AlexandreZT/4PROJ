import React, { useState, useEffect } from 'react';
import {MODULE_CODE_LIST, NUMBER_OF_MODULES} from '../js/constant'

export default function Report() {
    const  [user, setUser] = useState({userId: null, data: null, status_code: null});

    function load_directory (userId, callback) {
        var axios = require('axios');

        var config = {
            method: 'get',
            url: "http://127.0.0.1:5000/student/"+userId+"/pedago"
        };
        
        axios(config)

        .then(function (response) {
            if (response) {
                callback(userId, response.data, response.status); // Return your data inside the callback function
            } else {
                callback(null); // Return null if data doesn't exists
            }
        }).catch(function (error) {  
            callback(userId, error.response.data, error.response.status);
        });
        
    }
    
    function updatedata (userId, data, status_code) { // Call load_directory to get your data
        console.log("userId, data, code", userId, data, status_code)
        setUser({...user, userId: userId, data: data, status_code: status_code});
        // continue here
    }

    function displayGrades (data) {
        if (user.status_code == 200) { 
            return Object.keys(MODULE_CODE_LIST).map( (index) => {
                if (data.hasOwnProperty(MODULE_CODE_LIST[index])){
                    return <td>{data[MODULE_CODE_LIST[index]]}</td>;
                } else {
                    return <td>null</td>;
                }
            }); 
        }
    }

    function displayModules ()  {
        return Object.keys(MODULE_CODE_LIST).map( (index) => {
            return <td>
                {MODULE_CODE_LIST[index]}
            </td>;
        });
    }
    
    function changeUserSelected(e) {
        let {name, value} = e.target;
        load_directory(value, updatedata) // call me only if needed on submit
    }

    // this hook will get called everytime when user has changed
    useEffect (() => { 
        // perform some action which will get fired everytime when user gets updated
        //    console.log('Current user:', user)
        }, [user]
    )

    return (
        <div>
            <div>
                <form>
                    <label>Select User:&nbsp;</label>
                    <input onChange={changeUserSelected} placeholder="Enter User Email or Id"/>                    
                </form>
            </div>
            <div>
                <table style={{width: "100%"}} border={2} cellPadding={4}>
                <thead>
                    <tr>
                        {displayModules()}                        
                    </tr>            
                </thead>
                <tbody>
                    {displayGrades(user.data)}
                </tbody> 
            </table>
            </div>
        </div>
    )
}