import React from "react";

import { Link } from "react-router-dom";
import { Layout, Menu } from "antd";

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
        <Menu.Item key="4">Login / Signup</Menu.Item>
      </Menu>
    </Header>
  );
};

export default HeaderComponent;
