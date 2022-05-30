import React, { useState, useEffect } from 'react';

export default function Directory() {

    const  [state, setState] = useState({user_filter: "users", data_displayed: null, data: null}); // users by default or by types

    function load_directory (callback) {
        if (state.data == null) { // hack to stop requesting infiniti loop (function still called)
            var axios = require('axios');

            var config = {
                method: 'get',
                url: "http://127.0.0.1:5000/users" // https://4projgroup24.pythonanywhere.com/users" // "http://127.0.0.1:5000/users // + state.user_filter // if uing filter
            };
            
            axios(config)

            .then(function (response) {
                if (response) {
                    callback(response.data); // Return your data inside the callback function
                } else {
                    callback(null); // Return null if data doesn't exists
                }
            }).catch(function (error) {
                console.log(error);
            });
        }
    }
    
    
    load_directory(function (mydata) { // Call load_directory to get your data
        setState({...state, data: mydata});
        // continue here
    })

    function displayUsers(data) {
        if (data != null) {
            return Object.keys(data).map( (id) => {
              return <tr>
                {/* <td>{id}</td> */}
                <td>{data[id]["firstname"].charAt(0).toUpperCase() + data[id]["firstname"].substr(1).toLowerCase()}</td>
                <td>{data[id]["lastname"].toUpperCase()}</td>
                <td>{data[id]["email"]}</td>
                <td>{data[id]["user_type"].charAt(0).toUpperCase() + data[id]["user_type"].substr(1).toLowerCase()}</td>
              </tr>;
            });
        } else {
            return <p>data is not available</p>;
        }
    }

    useEffect(() => {
    },  [state]);
    
    return (
        <div>
            <table style={{width: "100%"}} border={2} cellPadding={4}>
                <thead>
                    <tr>
                        {/* <td>id</td> */}
                        <td>firstname</td>
                        <td>lastname</td>
                        <td>email</td>
                        <td>user_type</td>
                    </tr>            
                </thead>
                <tbody>
                    {displayUsers(state.data)}
                </tbody> 
            </table>
        </div>
    )
}