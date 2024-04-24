import Image from "next/image";

import Footer from "@/components/Footer";
import LandingSteps from "@/components/steps";
import MaxWidthWrapper from "@/components/MaxWidthWrapper";
import Link from "next/link";

export default function Home() {
  return (
    <>
      <MaxWidthWrapper className="mb-12 mt-28 sm:mt-40 flex flex-col items-center justify-center text-center">
        {/* Hero */}
        <h1 className="max-w-4xl text-3xl font-bold md:text-6xl lg:text-7xl">
          About{" "}
          <Link href="/" className="hover:text-blue-600">
            News<span className="text-blue-600">AI</span>d{" "}
          </Link>
        </h1>
        <p className="mt-8 text-lg md:text-xl lg:text-2xl">
          NewsAid started as the brain child of four CS411 students: Kevin,
          Jason, Daniel, Olivia. Journalism is hard, and we knew that we can
          make it easier by leveraging the power of generative AI.{" "}
        </p>

        <p className="mt-5 text-lg md:text-xl lg:text-2xl">
          By taking user input about article preferences, we make calls to
          OpenAI's api and handle the creation and display of the generated
          article.{" "}
        </p>
      </MaxWidthWrapper>

      <div className="absolute inset-0 -z-10 h-full w-full bg-white bg-[linear-gradient(to_right,#f0f0f0_1px,transparent_1px),linear-gradient(to_bottom,#f0f0f0_1px,transparent_1px)] bg-[size:2rem_2rem]"></div>
      {/* Value Proposition */}
      <LandingSteps />
      <Footer />
    </>
  );
}
