import { BrowserRouter, Route } from "react-router-dom";
import { Routes } from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import Home from "./pages/Home";

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<MainLayout />}>
            <Route index element={<Home />} />
          
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
