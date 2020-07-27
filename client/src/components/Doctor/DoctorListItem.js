import React from "react";
import { Link } from "react-router-dom";
import { List } from 'antd';

const Doctor = (item) => (
  <List.Item key={item.id}>
    <h3><Link to={`/doctors/${item.id}`}>{item.name}</Link></h3>
    <p>Patients count: {item.patients_count}</p>
  </List.Item>
);

export default Doctor;