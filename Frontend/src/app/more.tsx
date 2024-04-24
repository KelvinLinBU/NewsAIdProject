import Image from "next/image";

import Footer from "@/components/Footer";
import LandingSteps from "@/components/steps";

{
  /* Divide more elements and put them in different components, figure out ways to change the look of the website */
}

export default function More() {
  return (
    <>
      <div className="absolute inset-0 -z-10 h-full w-full bg-white bg-[linear-gradient(to_right,#f0f0f0_1px,transparent_1px),linear-gradient(to_bottom,#f0f0f0_1px,transparent_1px)] bg-[size:2rem_2rem]"></div>
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
