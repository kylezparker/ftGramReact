import React, { useState } from "react";
import Header from './Header';
import Footer from './Footer';
import Share from './Share';
import CreateArea from './CreateArea';
import shares from '../shares';
import "./App.css";
// import bootstrap here


function App() {
    const [shares, setShares] = useState([]);

    function addShare(newShare) {
        setShares(prevNotes => {
            return [...prevNotes, newShare];
        });
    }

    function deleteShare(id) {
        setShares(prevNotes => {
            return prevNotes.filter((shareItem, index) => {
                return index !== id;
            });
        });
    }
    console.log(shares);
    return <div>
        <div className="header" >
            <Header />
        </div>
        <CreateArea onAdd={addShare} />
        {shares.map((shareItem, index) => {
            return (
                <Share
                    key={index}
                    id={index}
                    author={shareItem.author}
                    title={shareItem.title}
                    subtitle={shareItem.subtitle}
                    image={shareItem.image}
                    body={shareItem.body}
                    onDelete={deleteShare}
                />
            );
        })}
        <Footer />
    </div>
};

export default App;