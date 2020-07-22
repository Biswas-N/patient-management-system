import React from "react";
import { Redirect } from "react-router-dom";

const Callback = (props) => {
    var hash = props.location.hash;
    var hash_arr = hash.split("&")
    if (hash_arr[2] === "token_type=Bearer") {
        var token_arr = hash_arr[0].split("=")
        localStorage.setItem('bearer_token', token_arr[1])
    }

    return (
        <Redirect to="/" />
    )
}

export default Callback