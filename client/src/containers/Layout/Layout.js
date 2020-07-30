import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
import { Layout } from "antd";

import "./Layout.css";
import NavBar from "../../components/Header";

const { Content, Footer } = Layout;

const MyLayout = (props) => {
    return (
        <Router>
            <Layout className="layout">
                <NavBar />
                <Content style={{ padding: "0 50px" }}>
                    {props.children}
                </Content>
                <Footer style={{ textAlign: "center" }}>
                    Developed by Biswas Nandamuri
            </Footer>
            </Layout>
        </Router>
    )
};

export default MyLayout;