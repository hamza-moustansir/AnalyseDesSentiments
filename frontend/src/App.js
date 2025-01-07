import React, { useState } from "react";
import axios from "axios";
import { motion } from "framer-motion";
import "sweetalert2/dist/sweetalert2.min.css";
import SweetAlert from "./sweetalert";
import Cover from "./cover";

const App = () => {
  const [text, setText] = useState("");
  const [error, setError] = useState(false);
  const [sentiment, setSentiment] = useState(null);

  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  const handlePredict = async () => {
    if (!text) {
      setError("Entrer un sentiment");
      return;
    }

    setError(null);

    try {
      const response = await axios.post("http://localhost:5000/predict", {
        text: text,
      });
      setSentiment(response.data.sentiment);
    } catch (error) {
      console.error("Erreur lors de la prédiction :", error);
      setError("Erreur lors de la prédiction");
    }
  };

  return (
    <div className="container mx-auto p-4 flex flex-col justify-center items-center text-white h-screen">
      <Cover />
      <h1 className="text-4xl font-bold mb-3 text-center">
        Analyse des Sentiments
      </h1>
      <p className="text-sm md:text-lg font-normal md:font-medium mb-8 text-center">
        Entrez un texte pour analyser son sentiment.
      </p>

      <div className="flex flex-col md:flex-row justify-between mx-auto gap-4">
        <div className="mb-4">
          <label className="block mb-2 text-sm font-medium text-white">
            Entrer un texte :
          </label>
          <input
            type="text"
            value={text}
            onChange={handleTextChange}
            className="text-input text-black px-2 py-1 rounded border"
          />
        </div>
      </div>

      <motion.button
        whileHover={{ scale: 1.06 }}
        whileTap={{ scale: 0.95 }}
        onClick={handlePredict}
        className="bg-gray-500 text-white px-4 py-2 rounded mt-4 text-base"
      >
        Analyser le Sentiment
      </motion.button>

      {sentiment && (
        <SweetAlert sentiment={sentiment} />
      )}
      {error && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.6 }}
          className="text-red-400 py-4 text-base font-medium absolute bottom-24"
        >
          {error}
        </motion.div>
      )}
    </div>
  );
};

export default App;
