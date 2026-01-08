'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { apiClient } from '@/lib/api';

interface UnauthorizedHandlerProps {
  children: React.ReactNode;
}

export default function UnauthorizedHandler({ children }: UnauthorizedHandlerProps) {
  const router = useRouter();

  useEffect(() => {
    // Check if user is authenticated
    const token = apiClient.getToken();
    if (!token) {
      // Redirect to login if not authenticated
      router.push('/login');
      router.refresh();
    }
  }, [router]);

  return <>{children}</>;
}