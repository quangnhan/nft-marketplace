import { useEffect, useState } from "react";
import { BiUserCircle } from "react-icons/bi";
import { FiUser } from "react-icons/fi";
import { LuSettings } from "react-icons/lu";
import { MdLanguage } from "react-icons/md";
import { MdOutlineModeNight } from "react-icons/md";
import { InputSwitch } from "primereact/inputswitch";

interface UserButtonProps {
  onClick: () => void;
  scrollPosition: number;
}

function UserButton({ onClick, scrollPosition }: UserButtonProps) {
  const [isTooltipVisible, setIsTooltipVisible] = useState(false);
  const [isNightMode, setIsNightMode] = useState(
    localStorage.getItem("MainThem") === "dark" ? true : false
  );
  const [theme, setTheme] = useState(
    localStorage.getItem("MainThem") || "light"
  );

  const menuItems = [
    {
      title: "Profile",
      icon: <FiUser className="text-2xl" />,
    },
    {
      title: "br",
    },
    {
      title: "Settings",
      icon: <LuSettings className="text-2xl" />,
    },
    {
      title: "Language",
      icon: <MdLanguage className="text-2xl" />,
    },
    {
      title: "Night Mode",
      icon: <MdOutlineModeNight className="text-2xl" />,
    },
  ];

  const handleToggleTheme = (e: any) => {
    setIsNightMode(e.value);
    setTheme(theme === "dark" ? "light" : "dark");
  };

  useEffect(() => {
    localStorage.setItem("MainThem", theme);
    document.body.dataset.theme = theme;
  }, [theme]);

  return (
    <div
      className="relative"
      onMouseEnter={() => setIsTooltipVisible(true)}
      onMouseLeave={() => setIsTooltipVisible(false)}
    >
      <button
        onClick={onClick}
        className={`user-btn flex justify-center items-center px-3 rounded-xl h-12 min-w-12 transition-all ${
          scrollPosition > 0 ? "bg-color" : "bg-[#ffffff1f] hover:bg-gray-500"
        }`}
      >
        <BiUserCircle
          className={`text-2xl ${
            scrollPosition > 0 ? "text-color" : "text-white"
          }`}
        />
      </button>
      {isTooltipVisible && (
        <div className="absolute top-full right-0 bg-white text-black rounded-lg min-w-[245px] shadow-lg p-2">
          {menuItems.map((item, index) => (
            <div key={index}>
              {item.title === "br" ? (
                <hr className="my-2" />
              ) : item.title === "Night Mode" ? (
                <button className="flex justify-between items-center p-4 hover:bg-gray-100 transition-all w-full rounded-lg">
                  <div className="flex items-center gap-4">
                    {item.icon && item.icon}
                    <span className="text-base font-semibold">
                      {item.title}
                    </span>
                  </div>
                  <InputSwitch
                    checked={isNightMode}
                    onChange={handleToggleTheme}
                  />
                </button>
              ) : (
                <button className="flex items-center gap-4 p-4 hover:bg-gray-100 transition-all w-full rounded-lg">
                  {item.icon && item.icon}
                  <span className="text-base font-semibold">{item.title}</span>
                </button>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default UserButton;
