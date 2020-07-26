import axios from "axios";

export const loginUrl = `https://${process.env.REACT_APP_AUTH0_DOMAIN}/authorize?audience=${process.env.REACT_APP_AUDIENCE}&response_type=token&client_id=${process.env.REACT_APP_CLIENT_ID}&redirect_uri=${process.env.REACT_APP_REDIRECT_URI}&scope=openid%20profile`

const userInfoUrl = `https://${process.env.REACT_APP_AUTH0_DOMAIN}/userinfo`

export const getCurrentUser = () => {
    var token = localStorage.getItem("bearer_token")
    return axios.get(
        userInfoUrl,
        {
            headers: { "Authorization": `Bearer ${token}` }
        }
    )
}
