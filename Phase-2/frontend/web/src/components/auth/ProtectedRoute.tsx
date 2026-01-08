'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/components/providers/AuthProvider';
import { apiClient } from '@/lib/api';

interface ProtectedRouteProps {
  children: React.ReactNode;
  fallback?: React.ReactNode;
}

export default function ProtectedRoute({ children, fallback = null }: ProtectedRouteProps) {
  const router = useRouter();
  const { user, loading } = useAuth();

  useEffect(() => {
    // Only check authentication once loading is complete
    if (!loading) {
      const token = apiClient.getToken();
      if (!token || !user) {
        // Redirect to login if not authenticated
        router.push('/login');
        router.refresh();
      }
    }
  }, [user, loading, router]);

  // Show loading state while checking auth status
  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-lg">Loading...</div>
      </div>
    );
  }

  // If user is authenticated, render the protected content
  if (user) {
    return <>{children}</>;
  }

  // If not authenticated, return fallback or redirect (handled by useEffect)
  return fallback;
}