'use client';

import { useAuth } from '@/components/providers/AuthProvider';
import ProtectedRoute from '@/components/auth/ProtectedRoute';
import Link from 'next/link';
import { useState } from 'react';

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const { user, logout } = useAuth();
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const handleLogout = () => {
    logout();
  };

  return (
    <ProtectedRoute>
      {/* Mobile sidebar */}
      {sidebarOpen && (
        <div className="fixed inset-0 z-40 flex md:hidden">
          <div className="fixed inset-0 bg-gray-600 bg-opacity-75" onClick={() => setSidebarOpen(false)}></div>
          <div className="relative flex w-64 flex-1 flex-col bg-white">
            <div className="flex h-16 flex-shrink-0 items-center border-b border-gray-200 px-4">
              <span className="text-lg font-semibold text-gray-900">Todo App</span>
            </div>
            <div className="flex flex-1 flex-col overflow-y-auto">
              <nav className="mt-5 flex-1 space-y-1 bg-white px-2">
                <Link
                  href="/dashboard"
                  className="flex items-center rounded-md bg-blue-50 px-2 py-2 text-sm font-medium text-blue-700"
                >
                  Dashboard
                </Link>
                <button
                  onClick={handleLogout}
                  className="w-full text-left flex items-center rounded-md px-2 py-2 text-sm font-medium text-gray-600 hover:bg-gray-50 hover:text-gray-900 transition-colors duration-150"
                >
                  Logout
                </button>
              </nav>
            </div>
          </div>
        </div>
      )}

      <div className="flex h-screen">
        {/* Desktop sidebar */}
        <div className="hidden md:flex md:w-64 md:flex-col md:fixed md:inset-y-0">
          <div className="flex flex-1 flex-col overflow-y-auto border-r border-gray-200 bg-white">
            <div className="flex h-16 flex-shrink-0 items-center border-b border-gray-200 px-4">
              <span className="text-lg font-semibold text-gray-900">Todo App</span>
            </div>
            <div className="flex flex-1 flex-col overflow-y-auto">
              <nav className="mt-5 flex-1 space-y-1 bg-white px-2">
                <Link
                  href="/dashboard"
                  className="flex items-center rounded-md bg-blue-50 px-2 py-2 text-sm font-medium text-blue-700"
                >
                  Dashboard
                </Link>
                <button
                  onClick={handleLogout}
                  className="w-full text-left flex items-center rounded-md px-2 py-2 text-sm font-medium text-gray-600 hover:bg-gray-50 hover:text-gray-900 transition-colors duration-150"
                >
                  Logout
                </button>
              </nav>
            </div>
          </div>
        </div>

        {/* Main content */}
        <div className="md:pl-64 flex flex-col flex-1">
          {/* Top navigation bar */}
          <div className="sticky top-0 z-10 bg-white border-b border-gray-200">
            <div className="flex h-16 items-center justify-between px-4 sm:px-6 lg:px-8">
              <button
                type="button"
                className="mr-2 rounded-md p-2 text-gray-400 hover:text-gray-500 hover:bg-gray-100 md:hidden"
                onClick={() => setSidebarOpen(true)}
              >
                <span className="sr-only">Open sidebar</span>
                <svg
                  className="h-6 w-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  strokeWidth="1.5"
                  stroke="currentColor"
                  aria-hidden="true"
                >
                  <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                </svg>
              </button>
              <div className="flex items-center">
                <h1 className="text-xl font-semibold text-gray-900">Dashboard</h1>
              </div>
              <div className="flex items-center space-x-4">
                <span className="text-sm text-gray-600 hidden sm:block">
                  Welcome, {user?.name || user?.email}
                </span>
                <button
                  onClick={handleLogout}
                  className="text-sm font-medium text-blue-600 hover:text-blue-500 transition-colors duration-150"
                >
                  Logout
                </button>
              </div>
            </div>
          </div>

          {/* Page content */}
          <main className="flex-1 pb-8">
            {children}
          </main>
        </div>
      </div>
    </ProtectedRoute>
  );
}