import { Link } from "react-router-dom";

const Header = () => {
  return (
    <div className="flex justify-between w-full flex-col">
      <div className="flex p-4 justify-between w-full items-center border-b border-8">
        <div className="flex flex-row  justify-center items-center">
          <h1 className="border p-4 text-2xl">Mindeck</h1>
          <input
            type="text"
            placeholder="Search..."
            className="border ml-4 p-2 rounded-lg w-100 h-10"
          />
        </div>
        <div className="flex flex-row gap-4">
          <Link to="/login" className="ml-auto border p-2 rounded-lg">
            Login
          </Link>
          <Link to="/register" className="ml-auto border p-2 rounded-lg">
            Register
          </Link>
        </div>
      </div>
      <div className="flex w-full items-center p-4 gap-4">
        <Link to="/library" className="border p-2 ">
          библиотека
        </Link>
        <Link to="/desk" className=" border p-2 ">
          доска
        </Link>
        <Link to="/cards" className=" border p-2 ">
          карточки
        </Link>
        <Link to="/statistics" className=" border p-2 ">
          статистика
        </Link>
        <Link to="/settings" className=" border p-2">
          настройки
        </Link>
      </div>
    </div>  
  );
};

export default Header;