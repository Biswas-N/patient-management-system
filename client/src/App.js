import React from "react";
import { Switch, Route } from "react-router-dom";

import "./App.css";
import MyLayout from "./containers/Layout/Layout";
import Home from "./components/HomePage";
import Callback from "./components/Callback";
import Patients from "./containers/PatientsPage";
import Patient from "./containers/PatientPage";
import Doctors from "./containers/DoctorsPage";
import Doctor from "./containers/DoctorPage";


function App() {
  return (
    <MyLayout>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/callback" component={Callback} />
        <Route path="/patients/:id" component={Patient} />
        <Route path="/patients" component={Patients} />
        <Route path="/doctors/:id" component={Doctor} />
        <Route path="/doctors" component={Doctors} />
      </Switch>
    </MyLayout>
  );
}

export default App;
