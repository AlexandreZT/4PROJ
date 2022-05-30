import React, { useState, useEffect } from 'react';

export default function Report() {
    const  [user, setUser] = useState({userId: null, displayed_data: null});

    function load_directory (callback) {
        if (user.userId != null) { // hack to stop requesting infiniti loop (function still called)
            var axios = require('axios');

            var config = {
                method: 'get',
                url: "http://127.0.0.1:5000/student/"+user.userId+"/pedago"
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
        console.log("mydata", mydata)
        setUser({...user, displayed_data: mydata});
        // continue here
    })

    const display_pedago_data = () => {
        if (user.userId != null) { // 8pTwKdU0dFMOCDSydHHrLlMFp3n1
            return (
                <div>                
                    <p>{user.displayed_data["4AZUR"]}</p>
                </div> 
            )
        } 
    }
    
    function changeUserSelected(e) {
        let {name, value} = e.target;
        setUser({...user, userId: value, displayed_data: display_pedago_data()})
    }

    // this hook will get called everytime when user has changed
    useEffect (() => { 
        // perform some action which will get fired everytime when user gets updated
           console.log('Current user:', user)
        }, [user]
    )

    return (
        <div>
            <div>
            <label>Select User:&nbsp;</label>
            <input onChange={changeUserSelected}/>                
            {display_pedago_data(user.displayed_data)}
        </div>
        </div>
    )
}