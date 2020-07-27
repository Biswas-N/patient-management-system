import axios from 'axios';

const backend = axios.create({
    baseURL: `${process.env.REACT_APP_BACKEND}/api`,
    headers:{
        "Authorization": `Bearer ${localStorage.getItem("bearer_token")}`
    }
})

export default backend;