import logo from "../../assets/images/logo.png";
import {
  FaDiscord,
  FaInstagram,
  FaTiktok,
  FaTwitter,
  FaYoutube,
} from "react-icons/fa";

const Footer = () => {
  const listCommunity = [
    {
      icon: <FaTwitter className="text-white text-2xl" />,
    },
    {
      icon: <FaInstagram className="text-white text-2xl" />,
    },
    {
      icon: <FaDiscord className="text-white text-2xl" />,
    },
    {
      icon: <FaYoutube className="text-white text-2xl" />,
    },
    {
      icon: <FaTiktok className="text-white text-2xl" />,
    },
  ];
  const directories = [
    [
      {
        title: "Marketplace",
        child: [
          {
            title: "Art",
            path: "/art",
          },
          {
            title: "Gaming",
            path: "/gaming",
          },
          {
            title: "Memberships",
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
        ],
      },
    ],
    [
      {
        title: "My Account",
        child: [
          {
            title: "Profile",
            path: "",
          },
          {
            title: "Favorites",
            path: "",
          },
          {
            title: "Watchlist",
            path: "",
          },
          {
            title: "Studio",
            path: "",
          },
          {
            title: "OpenSea Pro",
            path: "",
          },
          {
            title: "Settings",
            path: "",
          },
        ],
      },
      {
        title: "Stats",
        child: [
          {
            title: "Rankings",
            path: "",
          },
          {
            title: "Activity",
            path: "",
          },
        ],
      },
    ],
    [
      {
        title: "Resources",
        child: [
          {
            title: "Blog",
            path: "",
          },
          {
            title: "Learn",
            path: "",
          },
          {
            title: "Help center",
            path: "",
          },
          {
            title: "Community standards",
            path: "",
          },
          {
            title: "Taxes",
            path: "",
          },
          {
            title: "Partner",
            path: "",
          },
          {
            title: "Developer platform",
            path: "",
          },
          {
            title: "Platform status",
            path: "",
          },
        ],
      },
    ],
    [
      {
        title: "Company",
        child: [
          {
            title: "About",
            path: "",
          },
          {
            title: "Careers",
            path: "",
          },
          {
            title: "Venture",
            path: "",
          },
        ],
      },
      {
        title: "Learn",
        child: [
          {
            title: "WWhat is an NFT?",
            path: "",
          },
          {
            title: "How to buy NFT",
            path: "",
          },
          {
            title: "What a NFT drops",
            path: "",
          },
          {
            title: "What is crypto wallet",
            path: "",
          },
          {
            title: "What is a blockchain",
            path: "",
          },
          {
            title: "What is web3",
            path: "",
          },
        ],
      },
    ],
  ];
  return (
    <div className="bg-footer font-inter px-8 pt-10 min-[1200px]:text-left">
      <div className="pb-10 border-b border-[#e5e8eb3f] min-[1200px]:flex justify-between gap-32">
        <div className="min-[1200px]:w-1/2 mb-2">
          <h4 className="my-4 text-white text-xl font-semibold">
            Stay in the loop
          </h4>
          <p className="text-white text-base">
            Join our mailing list to stay in the loop with our newest feature
            releases, NFT drops, and tips and tricks for navigating OpenSea.
          </p>
          <div className="flex items-center gap-2 mt-2">
            <input
              type="text"
              className="h-12 rounded-xl outline-none text-lg p-3 flex-1 font-medium border bg-header text-color"
              placeholder="Your email address"
            />
            <button className="h-12 w-[108px] text-white bg-[#2081E2] hover:bg-blue-500 rounded-lg text-base font-semibold">
              Sign up
            </button>
          </div>
        </div>

        <div className="min-[1200px]:w-1/2 mt-12 min-[1200px]:mt-0 min-[1200px]:text-left">
          <h4 className="my-4 text-white text-xl font-semibold">
            Join the community
          </h4>
          <div className="flex gap-2 max-[1200px]:justify-center">
            {listCommunity.map((item, key) => (
              <button
                key={key + "social"}
                className="btn-bg hover:bg-blue-500 flex items-center justify-center w-[54px] h-[54px] rounded-xl"
              >
                {item.icon}
              </button>
            ))}
          </div>
        </div>
      </div>

      <div className="min-[1200px]:flex gap-8 mt-16 font-inter border-b border-[#e5e8eb3f]">
        <div className="min-[1200px]:w-[30%] flex flex-col max-[1200px]:items-center mb-16">
          <img
            src={logo}
            alt="Logo"
            className="w-11 h-11 min-w-11 min-h-11 bg-white rounded-full"
          />
          <h4 className="text-3xl font-semibold text-white my-2">OpenSea</h4>
          <p className="text-base text-white font-medium">
            The world’s first and largest digital marketplace for crypto
            collectibles and non-fungible tokens (NFTs). Buy, sell, and discover
            exclusive digital items.
          </p>
        </div>
        <div className="min-[1200px]:w-[70%] grid grid-cols-4 gap-4">
          {directories.map((directory, index) => (
            <div className="col-span-1" key={index + "directories"}>
              {directory.map((categories, index) => (
                <div className="mb-10" key={index + "categories"}>
                  <h5 className="text-base font-semibold text-white">
                    {categories.title}
                  </h5>
                  {categories.child.map((item, index) => (
                    <p
                      key={index + "category"}
                      className="mt-3 text-sm font-medium text-white"
                    >
                      {item.title}
                    </p>
                  ))}
                </div>
              ))}
            </div>
          ))}
        </div>
      </div>

      <div className="flex justify-between py-4">
        <p className="text-xs font-medium text-white">© 2018 - 2024 Ozone Networks, Inc</p>
        <div className="flex gap-3">
          <p className="text-xs font-medium text-white">Privacy Policy</p>
          <p className="text-xs font-medium text-white">Term of Service</p>
        </div>
      </div>
    </div>
  );
};

export default Footer;
