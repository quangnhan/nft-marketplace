import image from "../../assets/images/image.avif";
import verify from "../../assets/icons/verified.png";
import { useNavigate } from "react-router-dom";

interface CardProps {
  verified?: boolean;
  title: string;
  floor: number;
  volume: number;
}

function Card({ verified = false, title, floor, volume }: CardProps) {
  const navigate = useNavigate();

  return (
    <div
      onClick={() => navigate("/card")}
      className={`col-span-1 rounded-lg bg-card font-inter cursor-pointer shadow-lg hover:transform hover:translate-y-[-8px] transition duration-200 ease-in-out`}
    >
      <img
        src={image}
        alt="Avatar"
        className="h-[60%] w-full object-cover rounded-t-lg"
      />
      <div className="p-4">
        <div className="flex items-center mb-4">
          <h5 className="text-color text-sm font-semibold text-left">
            {title}
          </h5>
          {verified && (
            <img
              src={verify}
              alt="Verified"
              className="w-4 h-4 min-w-4 min-h-4 ml-2"
            />
          )}
        </div>
        <div className="flex justify-between items-center">
          <div className="">
            <h5 className="text-sm text-[#B5B5B5] font-medium text-left">
              Floor
            </h5>
            <p className="text-lg font-semibold text-color">{floor} ETH</p>
          </div>
          <div>
            <h5 className="text-sm text-[#B5B5B5] font-medium text-left">
              24h volume
            </h5>
            <p className="text-lg font-semibold text-color">{volume} ETH</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Card;
