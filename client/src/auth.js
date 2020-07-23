import axios from "axios";

export const loginUrl = `https://${process.env.REACT_APP_AUTH0_DOMAIN}/authorize?audience=${process.env.REACT_APP_AUDIENCE}&response_type=token&client_id=${process.env.REACT_APP_CLIENT_ID}&redirect_uri=${process.env.REACT_APP_REDIRECT_URI}&scope=openid%20profile`

export const getCurrentUser = () => {
        var token = localStorage.getItem("bearer_token")
        if (token == null){
            return null
        }
        else {
            axios.get(
                `https://${process.env.REACT_APP_AUTH0_DOMAIN}/userinfo`,
                {
                    headers: {"Authorization": `Bearer ${token}`}
                }
            ).then(res => {
                return res.data
            })
        }
}
