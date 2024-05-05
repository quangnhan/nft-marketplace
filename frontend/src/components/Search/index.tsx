import { AiOutlineSearch } from "react-icons/ai";
import './Search.scss';

interface SearchProps {
  className: string;
}

function Search({ className }: SearchProps) {
  return (
    <div
      className={`bg-search ${className} flex items-center w-[468px] h-12 rounded-xl p-2 opacity-80 border border-transparent focus-within:border-gray-500 hover:opacity-100 hover:shadow focus-within:opacity-100`}
    >
      <AiOutlineSearch className={`${className} text-2xl font-semibold`} />
      <input
        type="search"
        className={`${className} w-full ml-1 bg-transparent outline-none`}
        placeholder="Search"
      />
    </div>
  );
}

export default Search;
