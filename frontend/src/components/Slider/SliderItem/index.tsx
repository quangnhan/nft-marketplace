import image from "../../../assets/images/slider.avif";
import verify from "../../../assets/icons/verified.png";

interface SliderItemProps {
  title: string;
  floor: number;
  verified?: boolean;
}

function SliderItem({ title, floor, verified = false }: SliderItemProps) {
  return (
    <div className="aspect-square rounded-lg cursor-pointer overflow-hidden relative font-inter shadow-lg">
      <img
        src={image}
        alt="Slider"
        className="rounded-lg hover:scale-105 transition-all"
      />
      <div className="absolute bottom-3 left-4 shadow">
        <div className="flex items-center">
          <p className="text-white text-lg font-semibold">{title}</p>
          {verified && (
            <img
              src={verify}
              alt="Verified"
              className="w-4 h-4 min-w-4 min-h-4 ml-2"
            />
          )}
        </div>
        <p className="text-white text-base text-left">Floor: {floor} ETH</p>
      </div>
    </div>
  );
}

export default SliderItem;
