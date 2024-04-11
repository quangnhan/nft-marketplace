import { Route, Routes } from "react-router-dom";
import HomePage from "../pages/Home";
import AboutPage from "../pages/About";
import CollectionsPage from "../pages/CollectionsPage";

const Router = () => {
    return (
        <Routes>
            <Route
                path="/"
                element={<HomePage />}
            />
            <Route
                path="/about"
                element={<AboutPage />}
            />
            <Route
                path="/collections"
                element={<CollectionsPage />}
            />
        </Routes>
    );
}

export default Router;