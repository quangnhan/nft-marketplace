import { Route, Routes } from "react-router-dom";
import HomePage from "../pages/Home";
import AboutPage from "../pages/About";

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
        </Routes>
    );
}

export default Router;