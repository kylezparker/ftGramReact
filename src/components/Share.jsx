import React from "react";

function Share(props) {
    function handleClick() {
        props.onDelete(props.id);
    }

    return (
        <div>
            <h1>{props.title}</h1>
            <p>{props.body}</p>
            <button onClick={handleClick}>DELETE</button>
        </div>
    );
}


export default Share;