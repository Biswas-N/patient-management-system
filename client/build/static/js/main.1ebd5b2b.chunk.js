(this.webpackJsonpclient=this.webpackJsonpclient||[]).push([[0],{158:function(e,t,a){e.exports=a(257)},163:function(e,t,a){},164:function(e,t,a){},165:function(e,t,a){},257:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),o=a(20),c=a.n(o),l=(a(163),a(33)),i=(a(164),a(35)),m=a(258),u=(a(165),a(45)),s=a(109),d=a(81),E=a(128),p=a(84),h=a.n(p),f="https://".concat("patient-management-system.au.auth0.com","/authorize?audience=").concat("pms","&response_type=token&client_id=").concat("Abg5B5WnSEID76r7LCAbIGsWlpJjipBw","&redirect_uri=").concat("http://patient-management-system-1603.herokuapp.com/callback","&scope=openid%20profile"),g="https://".concat("patient-management-system.au.auth0.com","/userinfo"),b=m.a.Header,y=function(e){var t=Object(n.useState)({currentUser:null}),a=Object(u.a)(t,2),o=a[0],c=a[1];Object(n.useEffect)((function(){null!=localStorage.getItem("bearer_token")&&function(){var e=localStorage.getItem("bearer_token");return h.a.get(g,{headers:{Authorization:"Bearer ".concat(e)}})}().then((function(e){c({currentUser:e.data})}))}),[]);var l=r.a.createElement(s.a,{theme:"dark",mode:"horizontal",style:{float:"right"}},r.a.createElement(s.a.Item,{key:"1"},r.a.createElement("a",{href:f},"Login / Signup")));return null!=o.currentUser&&(l=r.a.createElement(s.a,{theme:"dark",mode:"horizontal",style:{float:"right"}},r.a.createElement(s.a.Item,{key:"1"},r.a.createElement(i.b,{to:"/patients"},"Patients")),r.a.createElement(s.a.Item,{key:"2"},r.a.createElement(i.b,{to:"/doctors"},"Doctors")),r.a.createElement(s.a.Item,{key:"3",onClick:function(){c({currentUser:null}),localStorage.removeItem("bearer_token")}},r.a.createElement(d.a,{placement:"bottom",color:"#f50",title:"Click to logout!"},r.a.createElement(E.a,{style:{marginRight:"6px"},src:o.currentUser.picture}),"Hello, ".concat(o.currentUser.name))))),r.a.createElement(b,null,r.a.createElement("div",{style:{maxWidth:"800px",margin:"0 auto"}},r.a.createElement(i.b,{to:"/"},r.a.createElement("div",{className:"logo"})),l))},k=m.a.Content,v=m.a.Footer,w=function(e){return r.a.createElement(i.a,null,r.a.createElement(m.a,{className:"layout"},r.a.createElement(y,null),r.a.createElement(k,{style:{padding:"0 50px"}},e.children),r.a.createElement(v,{style:{textAlign:"center"}},"Developed by Biswas Nandamuri")))},S=a(100),I=function(){var e=Object(l.g)();return r.a.createElement("div",{className:"site-layout-content"},r.a.createElement("div",{style:{maxWidth:"450px",margin:"0 auto",textAlign:"center"}},r.a.createElement("h3",null,"No match for route ",r.a.createElement("code",null,e.pathname)),r.a.createElement(i.b,{to:"/"},r.a.createElement(S.a,{type:"primary"},"Back to Home"))))},j=a(260),O=a(259),x=j.a.Paragraph,N=function(){var e=localStorage.getItem("bearer_token"),t=r.a.createElement(r.a.Fragment,null,r.a.createElement("p",null,"Please login using the following credentials"),r.a.createElement("p",null,"Username: ",r.a.createElement("strong",null,"dean@test.com")," ",r.a.createElement("br",null)," Password: ",r.a.createElement("strong",null,"Dean@123")),r.a.createElement("p",null,"or"),r.a.createElement("p",null,"Username: ",r.a.createElement("strong",null,"doctor@test.com")," ",r.a.createElement("br",null)," Password: ",r.a.createElement("strong",null,"Doctor@123")),r.a.createElement("p",null,"or"),r.a.createElement("p",null,"Username: ",r.a.createElement("strong",null,"nurse@test.com")," ",r.a.createElement("br",null)," Password: ",r.a.createElement("strong",null,"Nurse@123")));if(null!=e){var a="https://jwt.io/#debugger-io?token=".concat(e);t=r.a.createElement(r.a.Fragment,null,r.a.createElement("p",null,"Store the below bearer token somewhere, it is ",r.a.createElement("strong",null,"needed during testing")," ",r.a.createElement("br",null),"if the submitted tokens are expired."),r.a.createElement(O.a,null,"Token Start"),r.a.createElement(x,{ellipsis:{rows:3,expandable:!0,symbol:"more"}},e),r.a.createElement(O.a,null,"Token End"),r.a.createElement("p",null,"Check auth token in ",r.a.createElement("a",{href:a,target:"_blank",rel:"noopener noreferrer"},"jwt.io")))}return r.a.createElement("div",{className:"site-layout-content"},r.a.createElement("div",{style:{maxWidth:"450px",margin:"0 auto",textAlign:"center"}},t))},C=function(e){var t=e.location.hash.split("&");if("token_type=Bearer"===t[3]){var a=t[0].split("=");localStorage.setItem("bearer_token",a[1])}return r.a.createElement(l.a,{to:"/"})},D=a(134),_=a(263),P=a(151),A=a(264),B=function(e){return r.a.createElement(_.b.Item,{key:e.id},r.a.createElement("h3",null,r.a.createElement(i.b,{to:"/patients/".concat(e.id)},e.name)),e.doctor_name?r.a.createElement("p",null,"Treated by ",r.a.createElement("strong",null,e.doctor_name)):r.a.createElement("p",null,"Yet to be treated."))},U=function(){return h.a.create({baseURL:"".concat("http://localhost:5000","/api"),headers:{Authorization:"Bearer ".concat(localStorage.getItem("bearer_token"))}})},L=function(e){var t=Object(n.useState)(1),a=Object(u.a)(t,2),o=a[0],c=a[1],l=Object(n.useState)({data:null}),i=Object(u.a)(l,2),m=i[0],s=i[1];Object(n.useEffect)((function(){U().get("/patients?page=".concat(o)).then((function(e){s({data:e.data})})).catch((function(t){e.history.push("/"),D.a.error("Please login first")}))}),[o,e.history]);var d=r.a.createElement("p",null,"Loading...");return null!=m.data&&(d=r.a.createElement(_.b,{header:r.a.createElement("h2",null,"All Patients ",r.a.createElement(S.a,{onClick:function(){return D.a.info("Sorry! Not yet implemented")},style:{float:"right"},type:"primary",shape:"round",icon:r.a.createElement(A.a,null)},"Create New")),footer:r.a.createElement(P.a,{defaultCurrent:o,showTotal:function(e,t){return"".concat(t[0],"-").concat(t[1]," of ").concat(e," patients")},onChange:function(e){return c(e)},total:m.data.total_patients}),itemLayout:"horizontal",dataSource:m.data.patients,renderItem:B})),r.a.createElement("div",{className:"site-layout-content"},d)},T=a(261),z=a(262),W=a(265),F=T.a.Panel;var J=function(e){var t=null==e.data.doctor?"Yet to be treated":r.a.createElement(r.a.Fragment,null,"Treated by ",r.a.createElement(i.b,{to:"/doctors/".concat(e.data.doctor.id)},e.data.doctor.name)),a="Nothing listed...";return 0!==e.data.medication.length&&(a=function(e){var t=JSON.parse(e);return r.a.createElement(_.b,{bordered:!0,dataSource:t,renderItem:function(e){return r.a.createElement(_.b.Item,null,e.name," - ",e.units)}})}(e.data.medication)),r.a.createElement(z.a,{ghost:!1,onBack:function(){return window.history.back()},title:e.data.name,subTitle:t,extra:[r.a.createElement(S.a,{key:"2",danger:!0,onClick:e.onDelete},"Delete"),r.a.createElement(S.a,{key:"1",type:"primary",onClick:e.onEdit},"Edit")]},r.a.createElement(W.a,{column:2},r.a.createElement(W.a.Item,{label:"Age"},e.data.age),r.a.createElement(W.a.Item,{label:"Gender"},e.data.gender)),r.a.createElement(T.a,null,r.a.createElement(F,{header:"Medication",key:"1"},a)))},H=function(e){var t=Object(n.useState)(null),a=Object(u.a)(t,2),o=a[0],c=a[1];Object(n.useEffect)((function(){U().get("/patients/".concat(e.match.params.id)).then((function(e){e.data.success&&c(e.data.patient)})).catch((function(t){e.history.push("/"),D.a.error("Please login first")}))}),[e.match.params.id,e.history]);return r.a.createElement("div",{className:"site-layout-content"},null!=o?r.a.createElement(J,{data:o,onDelete:function(){D.a.loading("Deleting..."),U().delete("/patients/".concat(e.match.params.id)).then((function(t){D.a.info("Deleted patient"),e.history.push("/patients")})).catch((function(e){D.a.error("Error while deleting patient")}))},onEdit:function(){return D.a.info("Sorry! Not yet implemented")}}):r.a.createElement("p",null,"Loading..."))},G=function(e){return r.a.createElement(_.b.Item,{key:e.id},r.a.createElement("h3",null,r.a.createElement(i.b,{to:"/doctors/".concat(e.id)},e.name)),r.a.createElement("p",null,"Patients count: ",e.patients_count))},R=function(e){var t=Object(n.useState)(1),a=Object(u.a)(t,2),o=a[0],c=a[1],l=Object(n.useState)({data:null}),i=Object(u.a)(l,2),m=i[0],s=i[1];Object(n.useEffect)((function(){U().get("/doctors?page=".concat(o)).then((function(e){s({data:e.data})})).catch((function(t){e.history.push("/"),D.a.error("Please login first")}))}),[o,e.history]);var d=r.a.createElement("p",null,"Loading...");return null!=m.data&&(d=r.a.createElement(_.b,{header:r.a.createElement("h2",null,"All Doctors ",r.a.createElement(S.a,{onClick:function(){return D.a.info("Sorry! Not yet implemented")},style:{float:"right"},type:"primary",shape:"round",icon:r.a.createElement(A.a,null)},"Create New")),footer:r.a.createElement(P.a,{defaultCurrent:o,showTotal:function(e,t){return"".concat(t[0],"-").concat(t[1]," of ").concat(e," patients")},onChange:function(e){return c(e)},total:m.data.total_doctors}),itemLayout:"horizontal",dataSource:m.data.doctors,renderItem:G})),r.a.createElement("div",{className:"site-layout-content"},d)},Y=T.a.Panel,M=function(e){var t=r.a.createElement(_.b,{bordered:!0,dataSource:e.data.patients,renderItem:function(e){return r.a.createElement(_.b.Item,null,r.a.createElement(i.b,{to:"/patients/".concat(e.id)},e.name))}}),a="Treated "+e.data.patients.length+" patients";return r.a.createElement(z.a,{ghost:!1,onBack:function(){return window.history.back()},title:e.data.name,subTitle:a,extra:[r.a.createElement(S.a,{key:"2",danger:!0,onClick:e.onDelete},"Delete"),r.a.createElement(S.a,{key:"1",type:"primary",onClick:e.onEdit},"Edit")]},r.a.createElement(W.a,{column:2},r.a.createElement(W.a.Item,{label:"Age"},e.data.age)),r.a.createElement(T.a,null,r.a.createElement(Y,{header:"Patients",key:"1"},t)))},$=function(e){var t=Object(n.useState)(null),a=Object(u.a)(t,2),o=a[0],c=a[1];Object(n.useEffect)((function(){U().get("/doctors/".concat(e.match.params.id)).then((function(e){e.data.success&&c(e.data.doctor)})).catch((function(t){e.history.push("/"),D.a.error("Please login first")}))}),[e.match.params.id,e.history]);return r.a.createElement("div",{className:"site-layout-content"},null!=o?r.a.createElement(M,{data:o,onDelete:function(){D.a.loading("Deleting..."),U().delete("/doctors/".concat(e.match.params.id)).then((function(t){D.a.info("Deleted doctor and associated patients"),e.history.push("/doctors")})).catch((function(e){D.a.error("Error while deleting patient")}))},onEdit:function(){return D.a.info("Sorry! Not yet implemented")}}):r.a.createElement("p",null,"Loading..."))};var q=function(){return r.a.createElement(w,null,r.a.createElement(l.d,null,r.a.createElement(l.b,{path:"/",exact:!0,component:N}),r.a.createElement(l.b,{path:"/callback",component:C}),r.a.createElement(l.b,{path:"/patients",exact:!0,component:L}),r.a.createElement(l.b,{path:"/patients/:id",component:H}),r.a.createElement(l.b,{path:"/doctors",exact:!0,component:R}),r.a.createElement(l.b,{path:"/doctors/:id",component:$}),r.a.createElement(l.b,{component:I})))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));c.a.render(r.a.createElement(q,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[158,1,2]]]);
//# sourceMappingURL=main.1ebd5b2b.chunk.js.map