import { useState } from "react";
import Header from "@components/header";
import Footer from "@components/footer";

function App() {
	const [uploadedImage, setUploadedImage] = useState<File | null>(null);
	const [outputImage, setOutputImage] = useState<string | null>(null);

	const submitImage = async () => {
		if (!uploadedImage) return;

		const formData = new FormData();
		formData.append("image", uploadedImage);
		try {
			const res = await fetch("http://localhost:3000/mirror", {
				method: "POST",
				body: formData,
			});
			if (!res.ok) {
				throw new Error("Failed to mirror image");
			}
			const blob = await res.blob();
			const img = URL.createObjectURL(blob);
			setOutputImage(img);
		} catch (error) {
			console.error("Error mirroring image:", error);
		}
	};

	const ImageContent = () => {
		if (outputImage) {
			return <img src={outputImage} className="object-scale-down sm:h-96 h-[400px] max-w-4/5" alt="Mirrored" />;
		} else if (uploadedImage) {
			return (
				<img
					src={URL.createObjectURL(uploadedImage)}
					className="object-scale-down sm:h-96 h-[400px] max-w-4/5"
					alt="Uploaded"
				/>
			);
		} else {
			return (
				<h1 className="text-2xl sm:text-4xl aspect-square w-full flex items-center justify-center p-10 border-2 border-black">
					Upload an Image
				</h1>
			);
		}
	};

	return (
		<>
			<Header />
			<main className="flex flex-col justify-center items-center w-full">
				<div className="flex justify-center items-center m-10">
					<ImageContent />
				</div>
				<div className="flex flex-col sm:flex-row justify-center items-center">
					<input
						type="file"
						accept="image/*"
						className="p-1 m-2 w-56 text-md"
						onChange={(e) => {
							if (!e.target.files) {
								return;
							}
							setUploadedImage(e.target.files[0]);
							setOutputImage(null);
						}}
					/>
					<button
						onClick={submitImage}
						className="bg-celadon rounded-xl border-black border-1 text-lg sm:text-xl px-2 py-1 sm:px-4 sm:py-2 m-1 text-center active:bg-dark-slate-green transition-all">
						Upload
					</button>
				</div>
			</main>
			<Footer />
		</>
	);
}

export default App;
