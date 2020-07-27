import React from "react";
import { Link } from "react-router-dom";
import { PageHeader, Button, Descriptions, Collapse, List } from 'antd';

const { Panel } = Collapse;

function parseMedication(medicationBlob) {
    const medicationJson = JSON.parse(medicationBlob)
    return (
        <List
            bordered
            dataSource={medicationJson}
            renderItem={item => (
                <List.Item>
                    {item.name} - {item.units}
                </List.Item>
            )}
        />
    )
}


const Patient = props => {
    const treatedBy = props.data.doctor == null ?
        "Yet to be treated" :
        (
            <>
                Treated by <Link
                    to={`/doctors/${props.data.doctor.id}`}>
                        {props.data.doctor.name}
                    </Link>
            </>
        )
    let medication = "Nothing listed..."
    if (props.data.medication.length !== 0) {
        medication = parseMedication(props.data.medication)
    }

    return (
        <PageHeader
            ghost={false}
            onBack={() => window.history.back()}
            title={props.data.name}
            subTitle={treatedBy}
            extra={[
                <Button key="2" danger onClick={props.onDelete}>Delete</Button>,
                <Button key="1" type="primary" onClick={props.onEdit}>Edit</Button>,
            ]}
        >
            <Descriptions column={2}>
                <Descriptions.Item label="Age">{props.data.age}</Descriptions.Item>
                <Descriptions.Item label="Gender">{props.data.gender}</Descriptions.Item>
            </Descriptions>
            <Collapse>
                <Panel header="Medication" key="1">
                    {medication}
                </Panel>
            </Collapse>
        </PageHeader>
    )
};

export default Patient;