import "./index.css";
import Upload from "./components/Upload";
import Loader from "./components/Loader";
import { useState } from "react";

function App() {
  const [upload, setUpload] = useState(false);
  const [download, setDownload] = useState(true);
  const [loading, setLoading] = useState(false);

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
          <Upload />
          <button
            className="btn"
            onClick={() => {
              setUpload(false);
              setDownload(false);
              setLoading(true);
              setTimeout(() => {
                setLoading(false);
                setDownload(true);
              }, 3000);
            }}
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
          <h1>The music is generated successfully ✅</h1>
          <h2>Click the button below to download the generated music</h2>
          <button className="btn">Download</button>
        </section>
      )}
    </>
  );
}

export default App;
