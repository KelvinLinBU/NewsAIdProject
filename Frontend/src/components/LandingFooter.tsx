import Link from "next/link";

const LandingFooter = () => {
  return (
    <footer className="z-10 border-t border-gray-200 bg-white/50 py-8 backdrop-blur-lg">
      <div className="mx-auto w-full max-w-screen-xl px-2.5 md:px-20 pt-10">
        <div className="xl:grid xl:grid-cols-5 xl:gap-8">
          <div className="space-y-8 xl:col-span-2">
            <Link href="/" className="font-bold">
              <span>News</span>
              <span className="text-blue-600">AI</span>
              <span>d</span>
            </Link>

            <p className="max-w-xs text-sm text-gray-500">
              A CS411 group project that leverages generative AI tools to help
              bring your journalistic ideas to life.
            </p>
            {}
          </div>
          <div className="mt-16 grid grid-cols-2 gap-8 xl:col-span-3 xl:mt-0">
            <div className="md:grid md:grid-cols-2 md:gap-8">
              <div></div>
              {/* Placeholder */}
              <div className="mt-10 md:mt-0">
                <ul role="list" className="mt-4 space-y-4">
                  <li></li>
                </ul>
              </div>
            </div>
            <div className="md:grid md:grid-cols-2 md:gap-8">
              {/* Placeholder */}
              <div></div>
              {/* Placeholder */}
              <div className="mt-10 md:mt-0">
                <h3 className="text-sm">
                  <Link
                    className="text-sm font-semibold text-gray-600 hover:text-gray-900 hover:font-bold"
                    href="https://github.com/KelvinLinBU/NewsAIdProject/tree/main"
                    target="_blank"
                  >
                    GitHub
                  </Link>
                </h3>
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default LandingFooter;
