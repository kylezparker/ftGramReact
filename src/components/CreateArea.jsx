import React, { useState } from "react";

function CreateArea(props) {

    const [share, setShare] = useState({
        author: "",
        title: "",
        subtitle: "",
        image: "",
        body: ""
    });

    function handleChange(event) {
        const { name, value } = event.target;

        setShare(prevNote => {
            return {
                ...prevNote,
                [name]: value
            };
        });
    }

    function submitShare(event) {
        props.onAdd(share);
        setShare({
            author: "",
            title: "",
            subtitle: "",
            image: "",
            body: ""
        });
        event.preventDefault();
    }


    return (
        <div>
            <form>
                <input name="author" onChange={handleChange} value={share.author} placeholder="Author" />
                <input name="title" onChange={handleChange} value={share.title} placeholder="Title" />
                <input name="subtitle" onChange={handleChange} value={share.subtitle} placeholder="Subtitle" />
                <input name="image" onChange={handleChange} value={share.image} placeholder="Image" />
                <textarea name="body" onChange={handleChange} value={share.body} placeholder="Insert message here" rows="3" />
                <button onClick={submitShare}>Add</button>
            </form>
        </div>
    );
}

export default CreateArea;