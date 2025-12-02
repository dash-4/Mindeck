const Footer = () => {
  const year = new Date().getFullYear();

  return (
    <footer className="border-t  border-8 w-full mt-auto">
      <div className="max-w-7xl mx-auto px-6 py-8">
        <div className="flex flex-col md:flex-row justify-between items-center gap-6 text-sm">
          <div className="flex items-center gap-2">
            
            <span className="font-semibold ">Mindeck</span>
            <span>© {year}. Все права защищены (или почти все)</span>
          </div>

          <div className="text-xs ">
            Сделано с ❤️ и интервальным повторением
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;