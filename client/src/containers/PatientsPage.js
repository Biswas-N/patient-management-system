import React, { useEffect, useState } from "react";
import { List, Pagination, Button, message } from 'antd';
import { PlusOutlined } from '@ant-design/icons';
import { Link } from "react-router-dom";

import Patient from "../components/Patient/PatientListItem";
import getBackendAxios from "../shared/axios";


const PatientsPage = (props) => {
    const [currentPage, setCurrentPage] = useState(1)
    const [state, setState] = useState({
        "data": null
    });
    useEffect(() => {
        var backend = getBackendAxios()
        backend.get(`/patients?page=${currentPage}`)
            .then(res => {
                setState({
                    "data": res.data
                })
            })
            .catch(err => {
                props.history.push("/");
                message.error("Please login first");
            });
    }, [currentPage])

    let list = (<p>Loading...</p>)
    if (state.data != null) {
        list = (
            <List
                header={
                    <h2>
                        All Patients <Link to="/patients/create">
                            <Button
                                style={{ float: "right" }}
                                type="primary"
                                shape="round"
                                icon={<PlusOutlined />}>
                                Create New
                            </Button>
                        </Link>
                    </h2>
                }
                footer={
                    <Pagination
                        defaultCurrent={currentPage}
                        showTotal={(total, range) => `${range[0]}-${range[1]} of ${total} patients`}
                        onChange={page => setCurrentPage(page)}
                        total={state.data.total_patients} />
                }
                itemLayout="horizontal"
                dataSource={state.data.patients}
                renderItem={Patient}
            />
        )
    }

    return (
        <div className="site-layout-content">
            {list}
        </div>
    );
};

export default PatientsPage;
