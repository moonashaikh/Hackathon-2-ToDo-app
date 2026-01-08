'use client';

import { createContext, useContext, useEffect, useState, ReactNode } from 'react';
import { useRouter } from 'next/navigation';
import { apiClient } from '@/lib/api';

interface AuthContextType {
  user: any | null; // In a real app, this would be strongly typed
  loading: boolean;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
  register: (username: string, email: string, password: string) => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

interface AuthProviderProps {
  children: ReactNode;
}

export function AuthProvider({ children }: AuthProviderProps) {
  const [user, setUser] = useState<any | null>(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    // Check if user is logged in on initial load
    const checkAuthStatus = async () => {
      try {
        // In a real implementation, we would validate the token with the backend
        // For now, we'll just check if a token exists
        const token = apiClient.getToken();
        if (token) {
          try {
            // Fetch user profile using the token to verify it's still valid and get user details
            const userProfile = await apiClient.getUserProfile();
            setUser(userProfile);

            // Update localStorage with fresh user data
            if (typeof window !== 'undefined') {
              localStorage.setItem('currentUser', JSON.stringify(userProfile));
            }
          } catch (error) {
            console.error('Failed to fetch user profile:', error);
            // If profile fetch fails, the token might be invalid/expired
            apiClient.removeToken();
            if (typeof window !== 'undefined') {
              localStorage.removeItem('currentUser');
            }
            setUser(null);
          }
        } else {
          setUser(null);
        }
      } catch (error) {
        console.error('Auth status check failed:', error);
        setUser(null);
      } finally {
        setLoading(false);
      }
    };

    checkAuthStatus();
  }, []);

  const login = async (username: string, password: string) => {
    try {
      const loginResponse = await apiClient.login({ username, password });

      // After login, fetch user profile to get full user details
      const userProfile = await apiClient.getUserProfile();

      setUser(userProfile);
      // Store user data in localStorage for persistence
      if (typeof window !== 'undefined') {
        localStorage.setItem('currentUser', JSON.stringify(userProfile));
      }
      router.push('/dashboard');
      router.refresh();
    } catch (error) {
      console.error('Login failed:', error);
      throw error;
    }
  };

  const register = async (username: string, email: string, password: string) => {
    try {
      const registerResponse = await apiClient.register({ username, email, password });

      // After registration, fetch user profile to get full user details
      const userProfile = await apiClient.getUserProfile();

      setUser(userProfile);
      // Store user data in localStorage for persistence
      if (typeof window !== 'undefined') {
        localStorage.setItem('currentUser', JSON.stringify(userProfile));
      }
      router.push('/dashboard');
      router.refresh();
    } catch (error) {
      console.error('Registration failed:', error);
      throw error;
    }
  };

  const logout = () => {
    apiClient.logout();
    setUser(null);
    // Clear user data from localStorage
    if (typeof window !== 'undefined') {
      localStorage.removeItem('currentUser');
    }
    router.push('/login');
    router.refresh();
  };

  const value = {
    user,
    loading,
    login,
    logout,
    register,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}