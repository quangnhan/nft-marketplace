import { Route, Routes } from "react-router-dom";
import HomePage from "../pages/Home";
import AboutPage from "../pages/About";
import CollectionsPage from "../pages/CollectionsPage";
import DetailPage from "../pages/DetailPage";

const Router = () => {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/about" element={<AboutPage />} />
      <Route path="/collections" element={<CollectionsPage />} />
      <Route path="/detail" element={<DetailPage />} />
    </Routes>
  );
};

export default Router;
