import { Layout, theme } from "antd";
import logo from "../../assets/images/logo.png";
import "./Header.scss";

const Header = () => {
    const {
        token: { colorBgContainer },
    } = theme.useToken();

    return (
        <Layout.Header
            style={{
                background: colorBgContainer,
            }}
            className="header"
        >
            <img src={logo} alt="logo" className="header-logo" />
        </Layout.Header>
    );
}

export default Header;