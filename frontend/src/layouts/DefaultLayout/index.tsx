import Footer from "../../components/Footer/Footer";
import Header from "../../components/Header/Header";

interface DefaultLayoutType {
  children: JSX.Element;
}

const DefaultLayout = ({ children }: DefaultLayoutType) => {
  return (
    <div className="w-full relative">
      <div className="sticky top-0 z-50">
        <Header />
      </div>
      <div className="flex-1 flex flex-col overflow-y-auto">{children}</div>
      <Footer />
    </div>
  );
};

export default DefaultLayout;
