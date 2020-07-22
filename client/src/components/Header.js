import React from "react";
import { Link } from "react-router-dom";
import { Layout, Menu } from "antd";

import { login_url } from "../auth";

const { Header } = Layout;

const HeaderComponent = () => {

  return (
    <Header>
      <div className="logo" />
      <Menu
        theme="dark"
        mode="horizontal"
        defaultSelectedKeys={["1"]}
        style={{ float: "right" }}
      >
        <Menu.Item key="1">
          <Link to="/">Home</Link>
        </Menu.Item>
        <Menu.Item key="2">
          <Link to="/patients">Patients</Link>
        </Menu.Item>
        <Menu.Item key="3">
          <Link to="/doctors">Doctors</Link>
        </Menu.Item>
        <Menu.Item key="4">
          <a href={login_url}>Login / Signup</a>
        </Menu.Item>
      </Menu>
    </Header>
  );
};

export default HeaderComponent;
