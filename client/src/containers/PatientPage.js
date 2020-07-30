import React, {useState, useEffect} from "react";
import { message } from "antd";

import PatientItem from "../components/Patient/PatientItem";
import getBackendAxios from "../shared/axios";

const Patient = (props) => {
    const [patient, setPatient] = useState(null)
    useEffect(() => {
        var backend = getBackendAxios();
        backend.get(`/patients/${props.match.params.id}`)
            .then(res => {
                if (res.data.success) {
                    setPatient(res.data.patient)
                }
            })
            .catch(err => {
                props.history.push("/");
                message.error("Please login first");
            });;
    }, [props.match.params.id])

    const onDeleteHandler = () => {
        message.loading('Deleting...');
        var backend = getBackendAxios();
        backend.delete(`/patients/${props.match.params.id}`)
            .then(res => {
                message.info('Deleted patient');
                props.history.push("/patients");
            })
            .catch(err => {
                message.error('Error while deleting patient');
            });
    }

    return (
        <div className="site-layout-content">
            {
                patient != null ?
                <PatientItem
                    data={patient}
                    onDelete={onDeleteHandler}
                    onEdit={() => console.log("Clicked Edit")}
                /> :
                <p>Loading...</p>
            }
        </div>
    )
};

export default Patient;