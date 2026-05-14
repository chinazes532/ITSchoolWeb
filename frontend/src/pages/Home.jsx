import Advantages from "../components/Advantages";
import Hero from "../components/Hero";
import { advantagesData } from "../utils/advantages";


export default function Home() {
  return (
    <>
      <Hero />
      <Advantages 
        items={advantagesData}
      />
    </>
  )
}
