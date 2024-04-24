import MaxWidthWrapper from "@/components/MaxWidthWrapper";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { buttonVariants } from "@/components/ui/button";
import Image from "next/image";

import Footer from "@/components/Footer";
import LandingSteps from "@/components/steps";

{
  /* Divide more elements and put them in different components, figure out ways to change the look of the website */
}

export default function Home() {
  return (
    <>
      <div className="absolute inset-0 -z-10 h-full w-full bg-white bg-[linear-gradient(to_right,#f0f0f0_1px,transparent_1px),linear-gradient(to_bottom,#f0f0f0_1px,transparent_1px)] bg-[size:2rem_2rem]"></div>

      <MaxWidthWrapper className="mb-12 mt-28 sm:mt-40 flex flex-col items-center justify-center text-center">
        {/* Hero */}
        <h1 className="max-w-4xl text-5xl font-bold md:text-6xl lg:text-7xl">
          Create <span className="text-blue-600">news</span>worthy articles with{" "}
          <span className="text-blue-600">AI</span>
        </h1>
        <p className="mt-5 max-w-prose text-zinc-700 sm:text-lg">
          Leveraging the power of <span className="font-semibold">AI</span>,{" "}
          NewsAId helps you effortlessly create{" "}
          <span className="font-semibold">compelling</span> and{" "}
          <span className="font-semibold">engaging</span> news articles.
        </p>

        {/* CTA w/ Shadcn UI Button Variants */}
        <div className="justify-center space-x-5">
          <Link
            className={buttonVariants({
              size: "lg",
              // variant: "outline",
              className: "mt-5",
            })}
            href="/login"
          >
            Get Started <ArrowRight className="ml-2 h-5 w-5" />{" "}
          </Link>

          <Link
            className={buttonVariants({
              size: "lg",
              // variant: "outline",
              className: "mt-5",
            })}
            href="/more"
          >
            Learn More{" "}
          </Link>
        </div>
      </MaxWidthWrapper>

      {/* Value Proposition */}
      <div>
        <div className="relative isolate">
          <div className="pointer-events-none absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"></div>
          <div className="mx-auto max-w-6xl px-6 lg:px-8 ">
            <div className="mt-16 flow-root sm:mt-24">
              <div className="-m-2 rounded-xl bg-gray-900/5 p-2 ring-1 ring-inset ring-gray-900/10 lg:-m-4 lg:rounded-2xl lg:p-4">
                <Image
                  src="/preview.jpg"
                  width={1200}
                  height={900}
                  alt="NewsAId Preview"
                  className="rounded-md bg-white p-2 sm:p-8 md:p-20 shadow-2xl ring-1 ring-gray-900/10"
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <LandingSteps />
      <Footer />
    </>
  );
}
