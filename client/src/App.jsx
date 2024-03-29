import "./index.css";
import Upload from "./components/Upload";
import Loader from "./components/Loader";
import { useState } from "react";

function App() {
  const [upload, setUpload] = useState(true);
  const [preview, setPreview] = useState(false);
  const [loading, setLoading] = useState(false);

  return (
    <>
      <header>
        <h1>RhythmGenius 🎹</h1>
      </header>
      {upload && (
        <section className="upload">
          <Upload />
          <button
            onClick={() => {
              setUpload(false);
              setPreview(false);
              setLoading(true);
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
      {preview && (
        <section className="preview">
          <h1>Preview</h1>
        </section>
      )}
    </>
  );
}

export default App;
