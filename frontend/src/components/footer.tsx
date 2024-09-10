const FooterLink = ({text, path}:{text:string, path:string}) => {
	return <a href={path} className="text-lg sm:text-xl p-2 m-1">{text}</a>
}

const Footer = () => {
	return (
		<footer className="flex justify-center bg-celadon text-dark-slate-green">
			<FooterLink text="Tutorial" path="/tutorial"/>
			<FooterLink text="About" path="/tuorial"/>
		</footer>
	)
}

export default Footer
