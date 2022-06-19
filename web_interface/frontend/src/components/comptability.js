import React, { useState, useEffect } from 'react';
import {BASE_URL} from '../js/constant'

export default function Comptability() {
    const  [user, setUser] = useState({userId: null, data: null, status_code: null});

    function load_directory (userId, callback) {
        var axios = require('axios');

        var config = {
            method: 'get',
            url: BASE_URL+"/student/"+userId+"/comptability"
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

    function displayComptability(data) {
        if (user.status_code===200) {
            return Object.keys(data).map( (id) => {
              return <td>{data[id].toString()}</td>;
            });
        } else {
            return <p>data is not available</p>;
        }
    }

    
    function changeUserSelected(e) {
        let {name, value} = e.target;
        load_directory(value.trim(), updatedata) // call me only if needed on submit
    }

    // this hook will get called everytime when user has changed
    useEffect (() => { 
        // perform some action which will get fired everytime when user gets updated
           console.log('Current user:', user.data)
        }, [user]
    )

    return (
        <div>
            <div>
                <form>
                    <label>Select Student:&nbsp;</label>
                    <input onChange={changeUserSelected} placeholder="Enter Student Email"/>                    
                </form>
            </div>
            <div>
                <table style={{width: "100%"}} border={2} cellPadding={4}>
                <thead>
                    <tr>
                        <td>compta paid</td>
                        <td>compta payment due</td>
                        <td>compta payment type</td>
                        <td>entry level</td>
                        <td>level of exit</td>
                        <td>still student</td>
                        <td>study lenght</td>
                        <td>year of entry</td>
                        <td>year of exit</td>
                    </tr>   
                </thead>
                <tbody>
                    {displayComptability(user.data)}
                </tbody> 
            </table>
            </div>
        </div>
    )
}