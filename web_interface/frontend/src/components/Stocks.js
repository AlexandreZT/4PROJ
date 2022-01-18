import React, { Component } from "react";

export default class Stocks extends Component {

    state = {
        stocks_data : {},
        displayed_action: "map",
        response: null                
    }

    displayStock = this.displayStock.bind(this)
    updateQuantity = this.updateQuantity.bind(this);
    getStockData = this.getStockData.bind(this);

    displayStocksData() {
        if (this.state.stocks_data) {       
            return Object.keys(this.state.stocks_data).map( (id) => {
                return <tr>
                <td>{id}</td>
                <td>{this.state.stocks_data[id]["name"]}</td>
                <td>{this.state.stocks_data[id]["quantity"]}</td>
                </tr>;
            });
        } else {
            return <p>data is not available</p>;
        }
    }

    getStockData() {
        var axios = require('axios');

        var config = {
        method: 'get',
        url: "http://127.0.0.1:5000/stocks"
        };
        
        axios(config)
        .then(response => this.setState({
            stocks_data: response.data
        }))
        .catch(function (error) {
            console.log(error);
        }); 
    }

    componentDidMount() {      
        this.getStockData()          
    }

    displayStock(){
        this.setState({ 
            displayed_action: "map",
            response: null,
            }, () => {
            this.getStockData()
        });
    }

    updateQuantity() {
        this.setState({ 
            displayed_action: "quantity",
            response: null,
            }, () => {
            this.getStockData()
        });      
    }

    submitUpdate = (e) => {
        e.preventDefault()
        fetch("http://127.0.0.1:5000/update-object-quantity", { // sign-up
            method: 'PUT',
            headers:{
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                name : e.target[0].value.toLowerCase().trim(),
                quantity : e.target[1].value.trim(),
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

    render() {
        return (
            <div >
                <div style={{textAlign: "center"}}>
                    <button style={{width: "calc(100% / 2)"}} onClick={this.displayStock}>Stock</button>
                    <button style={{width: "calc(100% / 2)"}} onClick={this.updateQuantity}>Update quantity</button>    
                </div>

                {this.state.displayed_action === "map" ?
                <table style={{width: "100%"}} border={2} cellPadding={5}>
                    <thead>            
                        <tr>
                            <td>id</td>
                            <td>name</td>
                            <td>quantity</td>
                        </tr>                                            
                    </thead>
                    <tbody>
                        {this.displayStocksData()}
                    </tbody> 
                </table>:
                
                this.state.displayed_action === "quantity" &&
                <div>
                    <br/>
                    <div className="auth-inner" >
                        <form onSubmit={this.submitUpdate}>
                            <h3>Update quantity</h3>
                            <div className="form-group">
                                <label>Name</label><br/>
                                <input type="text" className="form-control" placeholder="Enter Name" />
                            </div>
                            <br/>
                            <div className="form-group">
                                <label>Quantity</label><br/>
                                <input type="text" className="form-control" placeholder="Enter Quantity" />
                            </div>                       
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