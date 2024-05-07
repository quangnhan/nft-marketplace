import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import { publicRoutes } from "./routes";
import DefaultLayout from "./layouts/DefaultLayout";
import NotFound from "./pages/NotFound";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          {publicRoutes.map((route, index) => {
            return (
              <Route
                key={index}
                path={route.path}
                element={<DefaultLayout>{route.element}</DefaultLayout>}
              />
            );
          })}

          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
