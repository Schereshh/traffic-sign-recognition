import { useState } from "react";
import "./App.css";
import { predict } from "./api/apiClient";

function App() {
    const formData = new FormData();
    const [picture, setPicture] = useState<{ image: string }>();
    const [response, setResponse] = useState<any>();

    const handleClick = () => {
        if (picture != null) {
            formData.append("image", picture?.image);
            const message = predict(formData)
            return setResponse(
                <h3></h3>
            )
        }
        return setResponse(<h3 style={{
            color: 'red'
        }}>You have to upload a picture</h3>);
    };

    const onImageChange = (e: any) => {
        if (e.target.files && e?.target.files[0]) {
            const img = e?.target.files[0];
            setPicture({
                image: URL.createObjectURL(img),
            });
        }
    };

    return (
        <>
            <div>
                <h1>Traffic sign recognition</h1>
                <p>Upload a picture</p>
            </div>
            <div>
                <img src={picture?.image} />
            </div>
            <div>
                <input type="file" name="image" onChange={onImageChange} />
            </div>
            <div className="card">
                <button onClick={handleClick}>Upload</button>
                {response}
            </div>
            <p className="read-the-docs">Made by Seres Tamás</p>
        </>
    );
}

export default App;
