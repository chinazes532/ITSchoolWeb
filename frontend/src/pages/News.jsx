import News from "../components/News";
import { newsData } from "../utils/news";



export default function Home() {
  return (
    <>
      <News 
      newsData={newsData}
      />
    </>
  )
}
