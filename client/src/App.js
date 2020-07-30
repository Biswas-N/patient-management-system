import React from "react";
import { Switch, Route } from "react-router-dom";

import "./App.css";
import MyLayout from "./containers/Layout/Layout";
import NoMatch from "./components/404";

import Home from "./components/HomePage";
import Callback from "./components/Callback";
import Patients from "./containers/Patient/PatientsPage";
import Patient from "./containers/Patient/PatientPage";
import Doctors from "./containers/Doctor/DoctorsPage";
import Doctor from "./containers/Doctor/DoctorPage";


function App() {
  return (
    <MyLayout>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/callback" component={Callback} />
        <Route path="/patients" exact component={Patients} />
        <Route path="/patients/:id" component={Patient} />
        <Route path="/doctors" exact component={Doctors} />
        <Route path="/doctors/:id" component={Doctor} />
        <Route component={NoMatch} />
      </Switch>
    </MyLayout>
  );
}

export default App;
