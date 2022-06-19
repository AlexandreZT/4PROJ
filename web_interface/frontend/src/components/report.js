import React, { useState, useEffect } from 'react';
import {MODULE_CODE_LIST, BASE_URL} from '../js/constant'
import {VictoryPie} from 'victory';


export default function Report() {
    const  [user, setUser] = useState({userId: null, data: null, status_code: null, ects: null});

    function load_directory (userId, callback) {
        var axios = require('axios');

        var config = {
            method: 'get',
            url: BASE_URL+"/student/"+userId+"/pedago"
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
    
    function calculate_ects(data) {
        let ects = 0;
        Object.keys(data).forEach(key => {
            if (data[key]["note"] && data[key]["note"] > 10) { // if not undefined
                ects+=data[key]["ects"]
            } 
        });
        return ects
    }
    function updatedata (userId, data, status_code) { // Call load_directory to get your data
        // console.log("userId, data, code", userId, data, status_code)
        let ects = calculate_ects(data);
        setUser({...user, userId: userId, data: data, status_code: status_code, ects: ects}); // 
        // continue here
    }

    function displayPedago (data) {
        if (user.status_code===200) { 
            return Object.keys(MODULE_CODE_LIST).map( (index) => {
                if (data.hasOwnProperty(MODULE_CODE_LIST[index])){
                    return  <tr> {/* dynamique columns */}
                        <th scope="row">{MODULE_CODE_LIST[index]}</th> {/* key */}
                        <td>{data[MODULE_CODE_LIST[index]]["ects"]}</td> {/* ects */}
                        <td>{data[MODULE_CODE_LIST[index]]["note"]}</td> {/* note */}
                        <td>{data[MODULE_CODE_LIST[index]]["comment"]}</td> {/* comment */}
                    </tr> 
                } else {
                    return <td>null</td>;
                }   
            }); 
        } else {
            return <p>data is not available</p>;
        }
    }

    // function displayModules ()  {
    //     return Object.keys(MODULE_CODE_LIST).map( (index) => {
    //         return <td>
    //             {MODULE_CODE_LIST[index]}
    //         </td>;
    //     });
    // }
    
    function changeUserSelected(e) {
        let {name, value} = e.target;
        load_directory(value.trim(), updatedata) // call me only if needed on submit
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
                    <label>Select Student:&nbsp;</label>
                    <input onChange={changeUserSelected} placeholder="Enter Student Email"/>                    
                </form>
            </div>
            <div>
            <table style={{width: "100%"}} border={2} cellPadding={4}>    
                <tr> {/* static headers */}
                    <th scope="col">module</th>
                    <th scope="col">ects</th>
                    <th scope="col">note</th>
                    <th scope="col">comment</th>
                </tr>
                {displayPedago(user.data)}    
            </table>
            </div>
            <div style={{height: "300px"}}>
            { user.status_code===200 && user.ects!==null &&
                <VictoryPie
                    colorScale={["navy", "blue"]}
                    data={[
                        { x: "obtenu : "+(user.ects).toString(), y: user.ects },
                        { x: "restant : "+(60-user.ects).toString(), y: 60-user.ects },
                    ]}
                /> 
            }
            </div>
        </div>
    )
}