import { useState } from "react";
import { HiOutlineShoppingCart } from "react-icons/hi";
import { AiOutlineInfoCircle } from "react-icons/ai";
import { AiOutlineClose } from "react-icons/ai";

interface CardButtonProps {
    scrollPosition: number;
}

function CardButton({scrollPosition}: CardButtonProps) {
  const [isCartOpen, setIsCartOpen] = useState(false);
  const [cartItems, setCartItems] = useState([]);

  const toggleCart = () => {
    setIsCartOpen(!isCartOpen);
  };

  return (
    <div>
        <button
            className={`flex justify-center items-center px-3 rounded-xl h-12 min-w-12 transition-all ${
                scrollPosition > 0 ? "bg-color" : "bg-[#ffffff1f] hover:bg-gray-500"}`}
            onClick={toggleCart}
        >
            <HiOutlineShoppingCart className={`text-2xl ${scrollPosition > 0 ? "text-color" : "text-white"}`} />
        </button>
        {isCartOpen && (
            <div onClick={toggleCart} 
                className="fixed top-0 right-0 bottom-0 left-0 bg-black bg-opacity-40 flex justify-end">
                <div onClick={(event) => event.stopPropagation()} className="rounded-xl my-4 mr-4 bg-white min-w-[375px] flex flex-col">
                    <div className="flex justify-between p-6 border-b border-gray-300">
                        <div className="flex items-center">
                            <div className="mr-2 text-xl font-semibold">Your cart</div>
                            <AiOutlineInfoCircle className="text-xl text-gray-600"/>
                        </div>
                        <button onClick={toggleCart}>
                            <AiOutlineClose className="text-lg text-gray-900 hover:text-gray-600"/>
                        </button>
                    </div>
                    <div className="overflow-y-auto flex flex-col justify-between flex-1 px-6 pb-6">
                        {cartItems.length === 0 ? (<p className="text-base text-[#545454] mt-12 font-medium">Add items to get started</p>) : 
                        (
                            <ul>
                            {cartItems.map((item: any, index) => (
                                <li key={index}>{item.name}</li>
                            ))}
                            </ul>
                        )}
                        <button className={`rounded-lg flex justify-center items-center h-12 text-white text-base font-semibold ${cartItems.length ? 'bg-blue-600': 'bg-blue-200 cursor-auto'}`}>
                            Complete purchase
                        </button>
                    </div>
                </div>
            </div>
        )}
    </div>
  );
}

export default CardButton;
