import React, { useState, useEffect } from 'react';

export default function Directory() {

    const  [state, setState] = useState({user_filter: "users", data_displayed: null}); // users by default or by types

    function load_directory() {
        var axios = require('axios');

        var config = {
            method: 'get',
            url: 'http://127.0.0.1:5000/users' //+ state.user_filter
        };
        
        console.log(config)
        axios(config)
        // .then(response => (
        //     console.log(response.data)
        // ))
        .then(response => setState(
            {...state, data_displayed: response}
        ))
        .catch(function (error) {
            console.log(error);
        }); 
    }

    function displayUsers(){
        if (state.data_displayed) {
            return Object.keys(state.data_displayed).map( (id) => {
              return <tr>
                {/* <td>{id}</td> */}
                <td>{state.data_displayed[id]["firstname"]}</td>
                <td>{state.data_displayed[id]["lastname"]}</td>
                <td>{state.data_displayed[id]["email"]}</td>
                <td>{state.data_displayed[id]["user_type"]}</td>
              </tr>;
            });
        } else {
            return <p>data is not available</p>;
        }
    }

    useEffect(() => {
        load_directory()
        console.log(state.data_displayed)
    }, [state]);

    return (
        <div>
            {state.user_filter==="users"

            }
            <p>Directory</p>
        </div>
    )
}