import { Outlet } from "react-router-dom"
import Footer from "../components/Footer"
import Header from "../components/Header"

const MainLayout = () => {
    return(
        <div className="flex flex-col min-h-screen justify-center items-center w-[1200px] mx-auto">
            <Header />
            <main className="grow">{Outlet}</main>
            <Footer />
        </div>
    )
}

export default MainLayout