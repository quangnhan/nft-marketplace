import './App.css';
import { BrowserRouter } from "react-router-dom";
import { Layout } from "antd";
import Router from './router/Router';
import Header from './components/Header/Header';
import Footer from './components/Footer/Footer';

const { Content, Sider } = Layout;

function App() {
  return (
    <BrowserRouter>
      <Layout style={{ minHeight: "100vh" }}>
        <Header/>
        <Layout>
          <Content>
            <div
              style={{
                padding: 16,
                height: "100%",
              }}
            >
              <Router />
            </div>
          </Content>
        </Layout>
        <Footer/>
      </Layout>
    </BrowserRouter>
  );
}

export default App;
