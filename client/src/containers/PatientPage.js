import React, {useState, useEffect} from "react";

import PatientItem from "../components/Patient/PatientItem";
import backend from "../shared/axios";

const Patient = (props) => {
    const [patient, setPatient] = useState(null)
    useEffect(() => {
        backend.get(`/patients/${props.match.params.id}`)
            .then(res => {
                if (res.data.success) {
                    setPatient(res.data.patient)
                }
            })
    }, [props.match.params.id])

    return (
        <div className="site-layout-content">
            {
                patient != null ?
                <PatientItem
                    data={patient}
                    onDelete={() => console.log("Clicked Delete")}
                    onEdit={() => console.log("Clicked Edit")}
                /> :
                <p>Loading...</p>
            }
        </div>
    )
};

export default Patient;