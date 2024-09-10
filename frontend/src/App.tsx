import Header from "./components/header";
import Footer from "./components/footer";
import HomeContent from "./components/homeContent";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

function App() {
	const router = createBrowserRouter([
		{
			path: "/",
			element: <HomeContent />,
			children: [],
		},
	]);

	return (
		// <>
		// 	<Header />
		// 	<main className="flex flex-col justify-center items-center w-full">
		// 		<Router>
		// 			<Switch>
		// 				<Route path="/test" Component={<HomeContent />} />
		// 			</Switch>
		// 		</Router>
		// 	</main>
		// 	<Footer />
		// </>
		<RouterProvider router={router} />
	);
}

export default App;
