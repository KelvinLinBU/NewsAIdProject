const LandingSteps = () => {
  return (
    <div className="mx-auto mb-32 mt-10 max-w-5xl sm:mt-20">
      <div className="mb-12 px-6 lg:px-8">
        <div className="mx-auto max-w-2xl sm:text-center">
          <h2 className="mt-2 font-bold text-4xl text-gray-900 sm:text-5xl">
            Only <span className="text-blue-600">Three</span> Steps
          </h2>
        </div>
      </div>

      {/* Actual steps */}
      <ol className="my-8 space-y-4 pt-8 md:flex md:space-x-12 md:space-y-0">
        <li className="md:flex-1">
          <div className="flex flex-col space-y-2 border-l-4 border-zinc-300 py-2 pl-4 md:border-l-0 md:border-t-2 md:pb-0 md:pl-0 md:pt-4">
            <span className="text-sm font-medium text-blue-600">Step 1</span>
            <span className="text-xl font-semibold">Create an account</span>
            <span className="mt-2 text-zinc-700">
              By creating an account, you&apos;ll be able to save your writing
              preferences and ensure uniformity across all your articles.
            </span>
          </div>
        </li>
        <li className="md:flex-1">
          <div className="flex flex-col space-y-2 border-l-4 border-zinc-300 py-2 pl-4 md:border-l-0 md:border-t-2 md:pb-0 md:pl-0 md:pt-4">
            <span className="text-sm font-medium text-blue-600">Step 2</span>
            <span className="text-xl font-semibold">Set your preferences</span>
            <span className="mt-2 text-zinc-700">
              You get to choose the tone, style, and length of the article. You
              can even include sentences you want to be included!
            </span>
          </div>
        </li>
        <li className="md:flex-1">
          <div className="flex flex-col space-y-2 border-l-4 border-zinc-300 py-2 pl-4 md:border-l-0 md:border-t-2 md:pb-0 md:pl-0 md:pt-4">
            <span className="text-sm font-medium text-blue-600 justify-center">
              Step 3
            </span>
            <span className="text-xl font-semibold">
              We&apos;ll do the rest
            </span>
            <span className="mt-2 text-zinc-700">
              It&apos;s that simple. We&apos;ll generate a news article for you
              based on your preferences.
            </span>
          </div>
        </li>

        <li className="md:flex-1">
          <div className="flex flex-col space-y-2 border-l-4 border-zinc-300 py-2 pl-4 md:border-l-0 md:border-t-2 md:pb-0 md:pl-0 md:pt-4">
            <span className="text-sm font-medium text-blue-600">Step 4</span>
            <span className="text-xl font-semibold">Share with friends</span>
            <span className="mt-2 text-zinc-700">
              Now that you have your article, you can share it with your
              friends!
            </span>
          </div>
        </li>
      </ol>
    </div>
  );
};

export default LandingSteps;
