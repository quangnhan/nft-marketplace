import React, { useEffect, useState } from "react";
import Card from "../components/Card";
import Slider from "../components/Slider";
import { Swiper, SwiperSlide } from "swiper/react";
import { Navigation } from "swiper/modules";
import { Link } from "react-router-dom";

const HomePage: React.FC = () => {
  const [numCard, setNumCard] = useState(5);

  const handleResize = () => {
    const width = window.innerWidth;

    if (width >= 1200) {
      setNumCard(5);
    } else if (width >= 1024) {
      setNumCard(4);
    } else if (width >= 768) {
      setNumCard(3);
    } else if (width >= 560) {
      setNumCard(2);
    } else {
      setNumCard(1);
    }
  };
  useEffect(() => {
    handleResize();

    window.addEventListener("resize", handleResize);

    return () => window.removeEventListener("resize", handleResize);
  }, []);
  return (
    <div className="bg-primary font-inter py-10">
      <Slider />
      <div className="mt-8 px-8">
        <h3 className="text-color text-xl font-bold text-left">
          Notable collections
        </h3>
        <Swiper
          slidesPerView={numCard}
          spaceBetween={30}
          pagination={{
            clickable: true,
          }}
          navigation={true}
          modules={[Navigation]}
          className="card-swiper py-4"
        >
          <SwiperSlide>
            <Link to="/detail">
              <Card
                verified
                title="Parallel Alpha [Base]"
                floor={0.5}
                volume={0.15}
              />
            </Link>
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
        </Swiper>
      </div>

      <div className="mt-8 px-8">
        <h3 className="text-color text-xl font-bold text-left">
          Top Collector Buys Today
        </h3>
        <Swiper
          slidesPerView={numCard}
          spaceBetween={30}
          pagination={{
            clickable: true,
          }}
          navigation={true}
          modules={[Navigation]}
          className="mySwiper py-4"
        >
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
        </Swiper>
      </div>

      <div className="mt-8 px-8">
        <h3 className="text-color text-xl font-bold text-left">
          Trending in Art
        </h3>
        <Swiper
          slidesPerView={numCard}
          spaceBetween={30}
          pagination={{
            clickable: true,
          }}
          navigation={true}
          modules={[Navigation]}
          className="mySwiper py-4"
        >
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
          <SwiperSlide>
            <Card
              verified
              title="Parallel Alpha [Base]"
              floor={0.5}
              volume={0.15}
            />
          </SwiperSlide>
        </Swiper>
      </div>
    </div>
  );
};

export default HomePage;
