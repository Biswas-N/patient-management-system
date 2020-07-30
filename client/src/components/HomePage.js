import React from "react";
import { Typography, Divider } from 'antd';

const { Paragraph } = Typography;


const Home = () => {
  const token = localStorage.getItem("bearer_token")

  let content = (
    <>
      <p>Please login using the following credentials</p>
      <p>Username: <strong>dean@test.com</strong> <br /> Password: <strong>Dean@123</strong></p>
      <p>or</p>
      <p>Username: <strong>doctor@test.com</strong> <br /> Password: <strong>Doctor@123</strong></p>
      <p>or</p>
      <p>Username: <strong>nurse@test.com</strong> <br /> Password: <strong>Nurse@123</strong></p>
    </>
  )
  if (token != null) {
    const jwtLink = `https://jwt.io/#debugger-io?token=${token}`;
    content = (
      <>
        <p>Store the below bearer token somewhere, it is <strong>needed during testing</strong> <br />if the submitted tokens are expired.</p>
        <Divider>Token Start</Divider>
        <Paragraph ellipsis={{ rows: 3, expandable: true, symbol: 'more' }}>
          {token}
        </Paragraph>
        <Divider>Token End</Divider>
        <p>Check auth token in <a href={jwtLink} target="_blank"  rel="noopener noreferrer">jwt.io</a></p>
      </>
    );
  }

  return (
    <div className="site-layout-content">
      <div style={{ maxWidth: "450px", margin: "0 auto", textAlign: "center" }}>
        {content}
      </div>
    </div>
  );
};

export default Home;
