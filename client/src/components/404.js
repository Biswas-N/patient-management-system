import React from "react";
import { Link, useLocation } from "react-router-dom";
import { Button } from "antd";

const NoMatch = () => {
    const location = useLocation();
    return (
        <div className="site-layout-content">
            <div style={{ maxWidth: "450px", margin: "0 auto", textAlign: "center" }}>
                <h3>
                    No match for route <code>{location.pathname}</code>
                </h3>
                <Link to="/">
                    <Button type="primary">Back to Home</Button>
                </Link>
            </div>
        </div>
    );

}

export default NoMatch;