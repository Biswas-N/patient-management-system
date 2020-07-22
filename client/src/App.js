import React from "react";
import "./App.css";

import NavBar from "./components/Header";
import Home from "./containers/HomePage/HomePage";
import Patients from "./containers/PatientsPage/PatientsPage";
import Doctors from "./containers/DoctorsPage/DoctorsPage";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Layout } from "antd";

const { Content, Footer } = Layout;

function App() {
  return (
    <Router>
      <Layout className="layout">
        <NavBar />
        <Content style={{ padding: "0 50px" }}>
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/patients" component={Patients} />
            <Route path="/doctors" component={Doctors} />
          </Switch>
        </Content>
        <Footer style={{ textAlign: "center" }}>
          Created by Biswas Nandamuri
        </Footer>
      </Layout>
    </Router>
  );
}

export default App;
