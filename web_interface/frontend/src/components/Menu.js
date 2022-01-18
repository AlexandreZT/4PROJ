import React, { Component } from "react";

export default class Menu extends Component {
    state = {
        menu_data : {},
        displayed_action: "create",
        response: null
    }

    selectCreateForMenu = this.selectCreateForMenu.bind(this);
    selectSearchForMenu = this.selectSearchForMenu.bind(this);
    selectUpdateForMenu = this.selectUpdateForMenu.bind(this);
    selectDeleteForMenu = this.selectDeleteForMenu.bind(this);

    searchProduct = (e) => {
        e.preventDefault()

        var axios = require('axios'); 

        if (e.target[0].value === "") {
            alert(`
            Enter Id !
            `)
        } else {
            axios({
                method: 'get',
                url: 'http://127.0.0.1:5000/menu/'+e.target[0].value
            })
            .then(response  =>
                this.setState({
                    menu_data: response.data
                })
            ) 
        }                
    } 

    createProduct = (e) => {
      e.preventDefault()
      if (e.target[0].value === "" || e.target[0].value.length < 2 || // name min 2 len
          e.target[1].value === "" || e.target[1].value.length < 2 || // description min 2 len
          e.target[2].value === "" || // price must be filled in
          e.target[3].value === "") { // type must be filled in
          alert(`
          Name length 2+
          Description length 2+
          Price must be filled in 
          `)
      } else {                
          fetch('http://127.0.0.1:5000/create-product', { // sign-up
              method: 'POST',
              headers:{
                  "Content-Type":"application/json"
              },
              body: JSON.stringify({
                  name : e.target[0].value.trim().toLowerCase(),
                  description : e.target[1].value.trim(),
                  price : e.target[2].value.trim(),
                  type : e.target[3].value.trim()
              }),
          }).then(async response => {
            this.setState({
                response: response.status
                })
            }
        ).catch(error => {
            this.setState({
                response: 500
            })
        });
      }                   
    }

    updateProduct = (e) => {
        e.preventDefault()
        if (e.target[0].value === "" || e.target[0].value.length < 2){ // id min 2 len
            alert(`
            Enter Id !
            `)
        } else {                
            fetch("http://127.0.0.1:5000/update-product-data-with-id", {
                method: 'PUT',
                headers:{
                    "Content-Type":"application/json"
                },
                body: JSON.stringify({
                    id : e.target[0].value.trim(),
                    name : e.target[1].value.trim().toLowerCase(),
                    description : e.target[2].value.trim(),
                    price : e.target[3].value.trim(),
                    type : e.target[4].value.trim()
                }),
            }).then(async response => {
                this.setState({
                    response: response.status
                })
                }
            ).catch(error => {
                this.setState({
                    response: 500
                })
            });
        }                   
    }

    deleteProduct = (e) => {
        e.preventDefault()
        if (e.target[0].value === "" || e.target[0].value.length < 2){ // id min 2 len
            alert(`
            Enter Id !
            `)
        } else {                
            fetch("http://127.0.0.1:5000/delete-product-with-id", {
                method: 'DELETE',
                headers:{
                    "Content-Type":"application/json"
                },
                body: JSON.stringify({
                    id : e.target[0].value.trim(),
                }),
            }).then(async response => {
                this.setState({
                    response: response.status
                })
                }
            ).catch(error => {
                this.setState({
                    response: 500
                })
            });
        }                   
    }

    selectCreateForMenu () {
        this.setState({
            displayed_action: "create",
            response: null,
            menu_data: {}
        })
    }

    selectSearchForMenu () {
        this.setState({
            displayed_action: "search",
            response: null,
            menu_data: {}
        })
    }
    
    selectUpdateForMenu () {
        this.setState({
            displayed_action: "update",
            response: null,
            menu_data: {}
        })
    }

    selectDeleteForMenu() {
        this.setState({
            displayed_action: "delete",
            response: null,
            menu_data: {}
        })
    }

    render() {
        return (
            <div>
                <div style={{textAlign: "center"}}>
                    <button style={{width: "calc(100% / 4)"}} onClick={this.selectCreateForMenu}>Create product</button>
                    <button style={{width: "calc(100% / 4)"}} onClick={this.selectSearchForMenu}>Search product</button>
                    <button style={{width: "calc(100% / 4)"}} onClick={this.selectUpdateForMenu}>Update product</button>
                    <button style={{width: "calc(100% / 4)"}} onClick={this.selectDeleteForMenu}>Delete product</button> 
                </div>
                <br/>

                {this.state.displayed_action === "create" ?
                
                <div className="auth-inner">
                    <form onSubmit={this.createProduct}>
                            <h3>Create product</h3>
                            <div className="form-group">
                                <label>Name</label><br/>
                                <input type="text" className="form-control" placeholder="Enter Name" />
                            </div>
                            <br/>
                            <div className="form-group">
                                <label>Description</label><br/>
                                <input type="text" className="form-control" placeholder="Enter Description" />
                            </div>
                            <br/>
                            <div className="form-group">
                                <label>Price</label><br/>
                                <input type="text" className="form-control" placeholder="Enter Price" />
                            </div>
                            <br/>                           
                            <div className="form-group">
                                <label>Category</label><br/>
                                <select name="type">
                                <option value="">Category</option>
                                    <option value="side">Side</option>
                                    <option value="pizza">Pizza</option>
                                    <option value="burger">Burger</option>
                                    <option value="salad">Salad</option>
                                    <option value="cake">Cake</option>
                                    <option value="cold drink">Cold drink</option>
                                    <option value="hot drink">Hot drink</option>
                                </select>
                            </div>
                            <br/>
                            <button type="submit" className="btn btn-primary btn-block">Create</button>
                            {   
                            this.state.response===null?
                            <p></p>:
                            this.state.response===200?
                            <p style={{color:"green"}}>Product created !</p>:
                            this.state.response===500 &&
                            <p style={{color:"red"}}>Something went wrong !</p>
                        }
                        </form>
                    </div>: this.state.displayed_action === "search" ?
                    <div className="auth-inner">
                        <form onSubmit={this.searchProduct}>                    
                            <h3>Search product</h3><br/>
                            <div className="form-group">
                                <label>Product Id*</label><br/>
                                <input type="text" placeholder="Search product by id"/>                            
                            </div>
                            <br/>
                            <button type="submit" className="btn btn-primary btn-block">Search</button>                                                         
                        </form>
                        {
                            this.state.menu_data != null ?
                            Object.keys(this.state.menu_data).map((key) => (
                                <p>{key} : {this.state.menu_data[key]}</p>
                            )) : 
                            <p style={{color:"red"}}>Something went wrong !</p>
                        }
                    </div>
                    : this.state.displayed_action === "update" ?
                    <div className="auth-inner">
                        <form onSubmit={this.updateProduct}>
                                <h3>Update product</h3>
                                <div className="form-group">
                                    <label>Product Id*</label><br/>
                                    <input type="text" className="form-control" placeholder="Enter Id" />
                                </div>
                                <br/>
                                <div className="form-group">
                                    <label>Name</label><br/>
                                    <input type="text" className="form-control" placeholder="New Name" />
                                </div>
                                <br/>
                                <div className="form-group">
                                    <label>Description</label><br/>
                                    <input type="text" className="form-control" placeholder="New Description" />
                                </div>
                                <br/>
                                <div className="form-group">
                                    <label>Price</label><br/>
                                    <input type="text" className="form-control" placeholder="New Price" />
                                </div>
                                <br/>                           
                                <div className="form-group">
                                    <label>Category</label><br/>
                                    <select name="type">
                                        <option value="">New Category</option>
                                        <option value="side">Side</option>
                                        <option value="pizza">Pizza</option>
                                        <option value="burger">Burger</option>
                                        <option value="salad">Salad</option>
                                        <option value="cake">Cake</option>
                                        <option value="cold drink">Cold drink</option>
                                        <option value="hot drink">Hot drink</option>                                            
                                    </select>
                                </div>
                                <br/>
                                <button type="submit" className="btn btn-primary btn-block">Update</button>
                                {   
                                    this.state.response===null?
                                    <p></p>:
                                    this.state.response===200?
                                    <p style={{color:"green"}}>Product updated !</p>:
                                    this.state.response===500 &&
                                    <p style={{color:"red"}}>Something went wrong !</p>
                                }
                            </form>
                        </div>
                    : this.state.displayed_action === "delete" &&
                    <div className="auth-inner">
                    <form onSubmit={this.deleteProduct}>                    
                        <h3>Delete product</h3><br/>
                        <div className="form-group">
                            <label>Product Id*</label><br/>
                            <input type="text" placeholder="Delete product by id"/>                            
                        </div>
                        <br/>
                        <button type="submit" className="btn btn-primary btn-block">Delete</button>
                        {   
                            this.state.response===null?
                            <p></p>:
                            this.state.response===200?
                            <p style={{color:"green"}}>Product deleted !</p>:
                            this.state.response===500 &&
                            <p style={{color:"red"}}>Something went wrong !</p>
                        }                                                     
                    </form>                    
                 </div>
                    }                    
            </div>
        );
    }
}