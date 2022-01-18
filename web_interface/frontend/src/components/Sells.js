import React, { Component } from "react";

export default class Sells extends Component {

    render() {
        return (
            <div >
                <div style={{textAlign: "center"}}>
                    <button style={{width: "calc(100% / 3)"}}>Service</button>
                    <button style={{width: "calc(100% / 3)"}}>Foods</button>
                    <button style={{width: "calc(100% / 3)"}}>Drinks</button>
                </div>
                Sells
            </div>
        );
    }
}