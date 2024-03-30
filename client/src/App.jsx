import "./index.css";
import Upload from "./components/Upload";
import Loader from "./components/Loader";
import { useState } from "react";
import axios from "axios";
import { v4 as uuidv4 } from "uuid";

function App() {
  const [upload, setUpload] = useState(true);
  const [download, setDownload] = useState(false);
  const [loading, setLoading] = useState(false);
  const [file, setFile] = useState(null);

  const handleChange = (event) => {
    setFile(event.target.files[0]);
    console.log(event.target.files[0]);
  };

  const handleUpload = async () => {
    let response;
    setUpload(false);
    setDownload(false);
    setLoading(true);
    const url = "http://localhost:8000/api/upload_file";
    const formData = new FormData();
    formData.append("file", file);
    const config = {
      headers: {
        "content-type": "multipart/form-data",
      },
      responseType: "arraybuffer",
    };
    try {
      response = await axios.post(url, formData, config);
      const blob = new Blob([response.data], { type: "audio/midi" });
      setFile(blob);
      setUpload(false);
      setDownload(true);
      setLoading(false);
    } catch (error) {
      setUpload(true);
      setDownload(false);
      setLoading(false);
    }
  };

  const handleDownload = () => {
    const url = window.URL.createObjectURL(file);
    const tempLink = document.createElement("a");
    tempLink.href = url;
    tempLink.setAttribute("download", `${uuidv4()}.mid`);
    document.body.appendChild(tempLink);
    tempLink.click();
    document.body.removeChild(tempLink);
    window.URL.revokeObjectURL(url);
  };

  return (
    <>
      <header>
        <h1
          onClick={() => {
            setUpload(true);
            setDownload(false);
            setLoading(false);
          }}
        >
          RhythmGenius 🎹
        </h1>
      </header>
      {upload && (
        <section className="upload">
          <Upload handleChange={handleChange} />
          <p>Selected File: {file ? file.name : "No file Selected"}</p>
          <button
            className="btn"
            onClick={() => {
              handleUpload();
            }}
            disabled={!file}
          >
            Generate
          </button>
        </section>
      )}
      {loading && (
        <section className="loading">
          <h1>Generating...</h1>
          <Loader />
        </section>
      )}
      {download && (
        <section className="download">
          <h1>Your melody is generated successfully ✅</h1>
          <h2>Click the button below to download the generated melody</h2>
          <button className="btn" onClick={handleDownload}>
            Download
          </button>
        </section>
      )}
      <footer>
        <p>
          🚀 Made with ❤️ by Kishan Kokal, Pratik Kithani, Shubham Mandal and,
          Harsh Punjabi. Big shoutout to Prof. Anagha Durugkar for keeping us on
          track! Peace out!✌️
        </p>
      </footer>
    </>
  );
}

export default App;
