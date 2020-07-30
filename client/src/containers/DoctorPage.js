import React, {useState, useEffect} from "react";
import { message } from "antd";

import DoctorItem from "../components/Doctor/DoctorItem";
import getBackendAxios from "../shared/axios";

const Doctor = (props) => {
    const [doctor, setDoctor] = useState(null)
    useEffect(() => {
        var backend = getBackendAxios()
        backend.get(`/doctors/${props.match.params.id}`)
            .then(res => {
                if (res.data.success) {
                    setDoctor(res.data.doctor)
                }
            })
            .catch(err => {
                props.history.push("/");
                message.error("Please login first");
            });
    }, [props.match.params.id, props.history])

    const onDeleteHandler = () => {
        message.loading('Deleting...');
        var backend = getBackendAxios();
        backend.delete(`/doctors/${props.match.params.id}`)
            .then(res => {
                message.info('Deleted doctor and associated patients');
                props.history.push("/doctors");
            })
            .catch(err => {
                message.error('Error while deleting patient');
            });
    }

    return (
        <div className="site-layout-content">
            {
                doctor != null ?
                <DoctorItem
                    data={doctor}
                    onDelete={onDeleteHandler}
                    onEdit={() => console.log("Clicked Edit")}
                /> :
                <p>Loading...</p>
            }
        </div>
    )
};

export default Doctor;