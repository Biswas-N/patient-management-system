import axios from 'axios';

const getBackendAxios = () => {
    return axios.create({
        baseURL: `${process.env.REACT_APP_BACKEND}/api`,
        headers:{
            "Authorization": `Bearer ${localStorage.getItem("bearer_token")}`
        }
    })
}

export default getBackendAxios;