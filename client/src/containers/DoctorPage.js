import React, {useState, useEffect} from "react";

import DoctorItem from "../components/Doctor/DoctorItem";
import backend from "../shared/axios";

const Doctor = (props) => {
    const [doctor, setDoctor] = useState(null)
    useEffect(() => {
        backend.get(`/doctors/${props.match.params.id}`)
            .then(res => {
                if (res.data.success) {
                    setDoctor(res.data.doctor)
                }
            })
    }, [props.match.params.id])

    return (
        <div className="site-layout-content">
            {
                doctor != null ?
                <DoctorItem
                    data={doctor}
                    onDelete={() => console.log("Clicked Delete")}
                    onEdit={() => console.log("Clicked Edit")}
                /> :
                <p>Loading...</p>
            }
        </div>
    )
};

export default Doctor;