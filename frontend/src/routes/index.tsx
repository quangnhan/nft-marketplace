import HomePage from "../pages/Home";
import DetailPage from "../pages/DetailPage";

// Public Routes
const publicRoutes = [
  { path: "/", element: <HomePage /> },
  { path: "/drops", element: <HomePage /> },
  { path: "/stats", element: <HomePage /> },
  { path: "/create", element: <HomePage /> },
  { path: "/detail", element: <DetailPage /> },

  // { path: "/races", element: <Races /> },
  // { path: "/race-result/:year/:grandPrix", element: <RaceResult /> },
  // { path: "/drivers", element: <Drivers /> },
  // { path: "/drivers/:driver", element: <Driver /> },
  // { path: "/teams", element: <Teams /> },
  // { path: "/awards", element: <Awards /> },
];
const privateRoutes = [{}];

export { publicRoutes, privateRoutes };
