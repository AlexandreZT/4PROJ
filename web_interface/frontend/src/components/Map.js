import React, { Component } from "react";

export default class Map extends Component {

    state = {
        tables_data : {},
        displayed_action: "map", 
        response: null          
    }

    displayMap = this.displayMap.bind(this);    
    displayCapacity = this.displayCapacity.bind(this);

    getMapData() {
        if (this.state.tables_data) {       
            return Object.keys(this.state.tables_data).map( (id) => {
                return <tr>
                <td>{id}</td>
                <td>{this.state.tables_data[id]["tableNumber"]}</td>
                <td>{this.state.tables_data[id]["capacity"]}</td>
                <td>{this.state.tables_data[id]["state"]}</td>
                </tr>
            });
        } else {
            return <p>data is not available</p>;
        }
    }

    componentDidMount(){
        this.loadData()
    }
    
    loadData() {
        var axios = require('axios');

        var config = {
        method: 'get',
        url: "http://127.0.0.1:5000/tables"
        };
        
        axios(config)
        .then(response => this.setState({
            tables_data: response.data
        }))
        .catch(function (error) {
            console.log(error);
        });  
    }

    displayMap(){
        this.setState({ 
            displayed_action: "map",
            response: null,
            }, () => {
            this.loadData()
        });
    }

    displayCapacity(){
        this.setState({ 
            displayed_action: "capacity",
            response: null,
            }, () => {
            this.loadData()
        });
    }


    updateCapacity = (e) => {
        e.preventDefault()
        if (e.target[0].value === "" || e.target[0].value.length < 2 || // id min 2 len
            e.target[1].value === "" || isNaN(e.target[1].value)){  // only numeric value
            alert(`
            Enter Id
            Capacity must be an integer
            `)
        } else {                
            fetch("http://127.0.0.1:5000/update-table-capacity-by-id", {
                method: 'PUT',
                headers:{
                    "Content-Type":"application/json"
                },
                body: JSON.stringify({
                    id : e.target[0].value.trim(),
                    capacity : e.target[1].value.trim(),
                }),
            }).then(async response => {
                this.setState({
                    response: response.status
                })
                }
            ).catch(error => {
                this.setState({
                    response: 404
                })
            });
        }                   
    }

    render() {
        return (
            <div >
                <div style={{textAlign: "center"}}>
                    <button style={{width: "calc(100% / 2)"}} onClick={this.displayMap}>Map</button>
                    <button style={{width: "calc(100% / 2)"}} onClick={this.displayCapacity}>Update capacity</button>
                </div>
                {this.state.displayed_action === "map" ?
                <table style={{width: "100%"}} border={2} cellPadding={5}>
                    <thead>            
                        <tr>
                            <td>id</td>
                            <td>table number</td>
                            <td>capacity</td>
                            <td>state</td>
                        </tr>                                            
                    </thead>
                    <tbody>
                        {this.getMapData()}
                    </tbody> 
                </table> :
                this.state.displayed_action === "capacity" &&
                <div>                    
                    <br/>
                    <div className="auth-inner">
                        <form onSubmit={this.updateCapacity}>
                            <h3>Update capacity</h3>
                            <div className="form-group">
                                <label>Table id</label><br/>
                                <input type="text" className="form-control" placeholder="Enter Id" />
                            </div>
                            <br/>
                            <div className="form-group">
                                <label>Capacity</label><br/>
                                <input type="text" className="form-control" placeholder="Enter Capacity" />
                            </div>
                            <br/>                                                   
                            <br/>
                            <button type="submit" className="btn btn-primary btn-block">Update</button>
                            {   
                            this.state.response===null?
                            <p></p>:
                            this.state.response===200?
                            <p style={{color:"green"}}>Capacity updated !</p>:
                            this.state.response===404 &&
                            <p style={{color:"red"}}>Something went wrong !</p>
                            }
                        </form>
                    </div>
                </div>
                }            
            </div>
        );
    }
}