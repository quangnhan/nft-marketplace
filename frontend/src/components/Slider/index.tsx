import { useEffect, useState } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { Autoplay, Navigation } from "swiper/modules";
import SliderItem from "./SliderItem";

function Slider() {
  const [activeTab, setActiveTab] = useState("All");
  const [numCard, setNumCard] = useState(4);

  const listTab = [
    {
      title: "All",
      path: "",
    },
    {
      title: "Art",
      path: "",
    },
    {
      title: "Gaming",
      path: "",
    },
    {
      title: "Memeberships",
      path: "",
    },
    {
      title: "PFPs",
      path: "",
    },
    {
      title: "Photography",
      path: "",
    },
    {
      title: "Music",
      path: "",
    },
  ];

  const handleClick = (tab: any) => {
    setActiveTab(tab.title);
  };

  const handleResize = () => {
    const width = window.innerWidth;

    if (width >= 1024) {
      setNumCard(4);
    } else if (width >= 768) {
      setNumCard(3);
    } else if (width >= 640) {
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
    <div className="px-8">
      <div className="flex items-center gap-2">
        {listTab.map((tab, key) => (
          <button
            className={`py-2 px-4 rounded-lg text-color text-base font-semibold bg-button-hover
          ${activeTab === tab.title ? "bg-button" : ""} 
          transition-all shadow-md`}
            key={key}
            onClick={() => handleClick(tab)}
          >
            {tab.title}
          </button>
        ))}
      </div>

      <Swiper
        slidesPerView={numCard}
        spaceBetween={30}
        pagination={{
          clickable: true,
        }}
        autoplay={{
          delay: 2500,
          disableOnInteraction: false,
        }}
        navigation={true}
        modules={[Autoplay, Navigation]}
        className="card-swiper py-4"
      >
        <SwiperSlide>
          <SliderItem title="Mystical Woodland" floor={0.15} verified />
        </SwiperSlide>
        <SwiperSlide>
          <SliderItem title="Mystical Woodland" floor={0.15} verified />
        </SwiperSlide>
        <SwiperSlide>
          <SliderItem title="Mystical Woodland" floor={0.15} verified />
        </SwiperSlide>
        <SwiperSlide>
          <SliderItem title="Mystical Woodland" floor={0.15} verified />
        </SwiperSlide>
        <SwiperSlide>
          <SliderItem title="Mystical Woodland" floor={0.15} verified />
        </SwiperSlide>
        <SwiperSlide>
          <SliderItem title="Mystical Woodland" floor={0.15} verified />
        </SwiperSlide>
        <SwiperSlide>
          <SliderItem title="Mystical Woodland" floor={0.15} verified />
        </SwiperSlide>
        <SwiperSlide>
          <SliderItem title="Mystical Woodland" floor={0.15} verified />
        </SwiperSlide>
      </Swiper>
    </div>
  );
}

export default Slider;
