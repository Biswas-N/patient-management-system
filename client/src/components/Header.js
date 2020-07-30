import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Layout, Menu, Tooltip, Avatar } from "antd";

import { loginUrl, getCurrentUser } from "../shared/auth";

const { Header } = Layout;

const HeaderComponent = (props) => {
  const [state, setState] = useState({
    currentUser: null
  });

  useEffect(() => {
    if (localStorage.getItem("bearer_token") != null) {
      getCurrentUser().then(res => {
        setState({
          currentUser: res.data
        })
      })
    }
  }, [])

  const logout = () => {
    setState({
      currentUser: null
    });
    localStorage.removeItem("bearer_token");
  }

  let menu = (
    <Menu
      theme="dark"
      mode="horizontal"
      style={{ float: "right" }}
    >
      <Menu.Item key="1">
        <a href={loginUrl}>Login / Signup</a>
      </Menu.Item>
    </Menu>
  )
  if (state.currentUser != null) {

    menu = (
      <Menu
        theme="dark"
        mode="horizontal"
        style={{ float: "right" }}
      >
        <Menu.Item key="1">
          <Link to="/patients">Patients</Link>
        </Menu.Item>
        <Menu.Item key="2">
          <Link to="/doctors">Doctors</Link>
        </Menu.Item>
        <Menu.Item key="3" onClick={logout}>
          <Tooltip
            placement="bottom"
            color={'#f50'}
            title={"Click to logout!"}
          >
            <Avatar style={{ marginRight: "6px" }} src={state.currentUser.picture} />
            {`Hello, ${state.currentUser.name}`}
          </Tooltip>
        </Menu.Item>
      </Menu>
    )
  }

  return (
    <Header>
      <div style={{
        maxWidth: "800px",
        margin: "0 auto"
      }}>
        <Link to="/"><div className="logo" /></Link>
        {menu}
      </div>
    </Header>
  );
};

export default HeaderComponent;
