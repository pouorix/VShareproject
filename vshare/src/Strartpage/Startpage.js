import React, { Component } from 'react'


import './Startpage.css'
import { Navbar, Nav } from 'react-bootstrap';

class startpage extends Component {

    render() {

        return (

            <div className="back_startpage">
                <div className="Main_div">
                    <Navbar collapseOnSelect expand="lg" style={{ backgroundColor: 'transparent', borderBottomColor: 'white', borderBottomStyle: 'solid' }}>
                        <Navbar.Brand href="#home" style={{ color: 'white', fontSize: '35px', fontWeight: 'bold' }}>Vsharee</Navbar.Brand>
                        <Navbar.Toggle aria-controls="responsive-navbar-nav " style={{ backgroundColor: 'white', color: 'white' }} />
                        <Navbar.Collapse id="responsive-navbar-nav" style={{ marginLeft: "30px" }}>
                            <Nav className="mr-auto" />

                            <Nav>
                                <Nav.Link href="/about" style={{ color: 'white', fontSize: '20px', paddingRight: '100px', fontWeight: 'bold' }}>About</Nav.Link>
                                <Nav.Link eventKey={2} href="#memes" style={{ color: 'white', fontSize: '20px', paddingRight: '100px', fontWeight: 'bold' }}>
                                    Contact
                                </Nav.Link>
                                <Nav.Link style={{ color: 'white', fontSize: '20px', paddingRight: '100px', fontWeight: 'bold' }}>Application</Nav.Link>
                                <Nav.Link eventKey={2} href="/login?#" style={{ color: 'white', fontSize: '20px', fontWeight: 'bold', borderStyle: 'solid', width: '200px', textAlign: 'center' }}>
                                    login/signup
                                </Nav.Link>
                            </Nav>
                        </Navbar.Collapse>
                    </Navbar>

                    <div className="container-lg" style={{ backgroundColor: "transparent", marginTop: '200px' }}>
                        <div className="row">
                            <div className="txt-container ">
                                <div className="txt-content col-sm-12 col-lg-8 col-xl-8 col-md-8" style={{ display: "block" }}>
                                    Vsharee is a web-base service which allows you to watch a video file with other users
                                    at the same time.
                                    You can talk through the movie with each other
                                    </div>
                                <a href="../login?#" style={{ color: 'black' }}>  <button style={{ cursor: 'pointer' }} className="btn_start">Get Start</button></a>
                            </div>
                        </div>

                    </div>
                </div>
            </div>

        )

    }
}
export default startpage;