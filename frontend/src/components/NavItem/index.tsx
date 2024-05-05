import { Link } from "react-router-dom";

interface NavItemProps {
  title: string;
  link: string;
}
function NavItem({ title, link }: NavItemProps) {
  return (
    <Link
      to={link}
      className="block text-left text-base text-primary font-semibold p-4 hover:bg-gray-100 rounded-lg whitespace-nowrap min-w-36"
    >
      {title}
    </Link>
  );
}

export default NavItem;
