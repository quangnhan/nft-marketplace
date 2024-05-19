import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "./Header.scss";
import logo from "../../assets/images/Logo Minty (1).png";
import metaMask from "../../assets/images/meta-mask.png";
import coinBase from "../../assets/images/walletlink-alternative.webp";
import walletConnect from "../../assets/images/walletconnect-alternative.webp";
import Search from "../Search";
import NavItem from "../NavItem";
import CardButton from "./CartButton";
import NavDropdown from "../NavDropdown";
import { MdOutlineWallet } from "react-icons/md";
import { PiArrowRight } from "react-icons/pi";
import { AiOutlineClose } from "react-icons/ai";
import UserButton from "./UserButton";

const Header = () => {
  const [isShowConnect, setIsShowConnect] = useState(false);
  const [scrollPosition, setScrollPosition] = useState(0);

  const toggleConnect = () => {
    setIsShowConnect(!isShowConnect);
  };

  useEffect(() => {
    const handleScroll = () => {
      const position = window.scrollY;
      setScrollPosition(position);
    };

    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <header
      className={`font-inter bg-opacity-60 h-[72px] px-8 py-[6px] flex justify-between items-center border-b border-b-[#e5e8eb3f] ${
        scrollPosition > 0 ? "bg-header scroll-header" : "bg-black"
      }`}
    >
      <div className="flex">
        <Link to="/" className="flex items-center gap-[10px]">
          <img
            src={logo}
            alt="Logo"
            className="w-10 h-10 min-w-10 min-h-10 rounded-full overflow-hidden"
          />
          <h4
            className={`text-2xl font-extrabold ${
              scrollPosition > 0 ? "title-color" : "text-white"
            }`}
          >
            NFT Marketplace
          </h4>
        </Link>
        <div className="h-8 w-[1px] mx-6 bg-white bg-opacity-20"></div>
        <nav
          className={`flex justify-center items-center gap-8 ${
            scrollPosition > 0 ? "text-color" : "text-white"
          }`}
        >
          <NavDropdown title="Drops" link="/drops">
            <NavItem title="Featured" link="/featured" />
            <NavItem title="Learn more" link="/learn-more" />
          </NavDropdown>
          <NavDropdown title="Stats" link="/stats">
            <NavItem title="Ranking" link="/ranking" />
            <NavItem title="Activity" link="/activity" />
          </NavDropdown>
          <NavDropdown title="Create" link="/create" />
        </nav>
      </div>
      <Search
        className={`${scrollPosition > 0 ? "text-color" : "text-white"}`}
      />
      <div className="flex gap-3">
        <button
          onClick={toggleConnect}
          className={`flex items-center gap-3 px-3 rounded-xl min-w-12 h-12 transition-all ${
            scrollPosition > 0 ? "bg-color" : "bg-[#ffffff1f] hover:bg-gray-500"
          }`}
        >
          <MdOutlineWallet className={`text-xl ${
            scrollPosition > 0 ? "text-color" : "text-white"}`} />
          <p className={`text-base font-semibold ${
            scrollPosition > 0 ? "text-color" : "text-white"}`}>Login</p>
        </button>
        <UserButton scrollPosition={scrollPosition} onClick={toggleConnect} />
        <CardButton scrollPosition={scrollPosition}/>
      </div>

      {/*Block Connect to */}
      {isShowConnect && (
        <div
          onClick={toggleConnect}
          className="fixed top-0 right-0 bottom-0 left-0 bg-black bg-opacity-60 font-inter flex justify-center items-center"
        >
          <div
            onClick={(event) => event.stopPropagation()}
            className="relative flex flex-col items-center w-[420px] px-6 py-[16px] rounded-lg bg-gray-100"
          >
            <button onClick={toggleConnect} className="absolute top-6 right-6">
              <AiOutlineClose className="text-lg text-gray-900 hover:text-gray-600 font-semibold" />
            </button>
            <img
              src={logo}
              alt="Logo"
              className="w-[100px] h-[100px] rounded-full mt-[52px] mb-6"
            />
            <p className="text-2xl font-semibold text-primary mb-6">
              Connect to NFT Marketplace
            </p>
            <div className="h-[52px] rounded-lg bg-white px-3 flex items-center w-full shadow-lg mb-4">
              <input
                type="text"
                className="outline-none flex-1"
                placeholder="Continue with email"
              />
              <button
                className={`flex justify-center items-center rounded-lg w-8 h-8 bg-blue-600 hover:bg-blue-500 transition-all`}
              >
                <PiArrowRight className="text-xl text-white" />
              </button>
            </div>
            <div className="mb-4 flex items-center w-full">
              <div className="h-[1px] bg-gray-300 flex-1"></div>
              <span className="text-xs text-[#545454] w-[30px] h-[30px] flex items-center justify-center">
                OR
              </span>
              <div className="h-[1px] bg-gray-300 flex-1"></div>
            </div>
            <div className="rounded-lg overflow-hidden w-full transition-all">
              <button className="px-4 py-3 bg-white flex items-center w-full hover:bg-gray-200 border-b border-b-gray-300">
                <img
                  src={metaMask}
                  alt="Meta Mask"
                  className="w-[30px] h-[30px] mr-4"
                />
                <p className="text-base font-semibold">MetaMask</p>
              </button>
              <button className="px-4 py-3 bg-white flex items-center w-full hover:bg-gray-200 border-b border-b-gray-300">
                <img
                  src={coinBase}
                  alt="Meta Mask"
                  className="w-[30px] h-[30px] mr-4"
                />
                <p className="text-base font-semibold">Coinbase Wallet</p>
              </button>
              <button className="px-4 py-3 bg-white flex items-center w-full hover:bg-gray-200">
                <img
                  src={walletConnect}
                  alt="Meta Mask"
                  className="w-[30px] h-[30px] mr-4"
                />
                <p className="text-base font-semibold">WalletConnect</p>
              </button>
            </div>
            <button className="mt-4 mb-10 text-base text-[#545454] font-medium">
              More wallet option
            </button>
          </div>
        </div>
      )}
    </header>
  );
};

export default Header;
