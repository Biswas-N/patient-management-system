import React, { useEffect, useState } from "react";
import { List, Pagination, Button } from 'antd';
import { PlusOutlined } from '@ant-design/icons';

import Doctor from "../components/Doctor/DoctorListItem";
import backend from "../shared/axios";

const DoctorsPage = () => {
    const [currentPage, setCurrentPage] = useState(1)
    const [state, setState] = useState({
        "data": null
    });
    useEffect(() => {
        backend.get(`/doctors?page=${currentPage}`)
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
                        All Doctors <Button
                            style={{float: "right"}}
                            type="primary"
                            shape="round"
                            href="/doctors/create"
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
                        total={state.data.total_doctors} />
                }
                itemLayout="horizontal"
                dataSource={state.data.doctors}
                renderItem={Doctor}
            />
        )
    }

    return (
        <div className="site-layout-content">
            {list}
        </div>
    )
};

export default DoctorsPage;