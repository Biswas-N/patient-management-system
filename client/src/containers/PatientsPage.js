import React, { useEffect, useState } from "react";
import { List, Pagination, Button } from 'antd';
import { PlusOutlined } from '@ant-design/icons';

import Patient from "../components/Patient/PatientListItem";
import backend from "../shared/axios";


const PatientsPage = () => {
    const [currentPage, setCurrentPage] = useState(1)
    const [state, setState] = useState({
        "data": null
    });
    useEffect(() => {
        backend.get(`/patients?page=${currentPage}`)
            .then(res => {
                setState({
                    "data": res.data
                })
            })
            .catch(err => { console.error(err) });
    }, [currentPage])

    let list = (<p>Loading...</p>)
    if (state.data != null) {
        list = (
            <List
                header={
                    <h2>
                        All Patients <Button
                            style={{float: "right"}}
                            type="primary"
                            shape="round"
                            href="/patients/create"
                            icon={<PlusOutlined />}>
                                Create New
                            </Button>
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
