export default function HomePage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-between p-24">
      <main className="flex flex-col items-center justify-center gap-8">
        <h1 className="text-4xl font-bold text-gray-900">Todo App</h1>
        <p className="text-lg text-gray-600 text-center">
          A professional todo management application
        </p>
        <div className="mt-8">
          <a
            href="/dashboard"
            className="rounded-md bg-blue-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
          >
            Go to Dashboard
          </a>
        </div>
      </main>
    </div>
  );
}