import React from "react";
import { Link } from "react-router-dom";
import { PageHeader, Button, Descriptions, Collapse, List } from 'antd';

const { Panel } = Collapse;


const Doctor = props => {
    let patients = (
        <List
            bordered
            dataSource={props.data.patients}
            renderItem={item => (
                <List.Item>
                    <Link to={`/patients/${item.id}`}>{item.name}</Link>
                </List.Item>
            )}
        />
    );

    let patientCount = "Treated " + props.data.patients.length + " patients"

    return (
        <PageHeader
            ghost={false}
            onBack={() => window.history.back()}
            title={props.data.name}
            subTitle={patientCount}
            extra={[
                <Button key="2" danger onClick={props.onDelete}>Delete</Button>,
                <Button key="1" type="primary" onClick={props.onEdit}>Edit</Button>,
            ]}
        >
            <Descriptions column={2}>
                <Descriptions.Item label="Age">{props.data.age}</Descriptions.Item>
            </Descriptions>
            <Collapse>
                <Panel header="Patients" key="1">
                    {patients}
                </Panel>
            </Collapse>
        </PageHeader>
    )
};

export default Doctor;