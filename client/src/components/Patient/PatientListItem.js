import React from "react";
import { Link } from "react-router-dom";
import { List } from 'antd';

const Patient = (item) => (
  <List.Item key={item.id}>
    <h3><Link to={`/patients/${item.id}`}>{item.name}</Link></h3>
    {
      item.doctor_name ? 
      <p>Treated by <strong>{item.doctor_name}</strong></p> :
      <p>Yet to be treated.</p>
    }
  </List.Item>
);

export default Patient;