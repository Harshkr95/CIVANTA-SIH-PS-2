import { createContext, useContext, useEffect, useState } from "react";
import { authService } from "../services/authService";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const stored = localStorage.getItem("civanta_user");

    if (stored) {
      try {
        setUser(JSON.parse(stored));
      } catch {
        localStorage.removeItem("civanta_user");
      }
    }

    setLoading(false);
  }, []);

  const login = async ({ email, password }) => {
    const response = await authService.login({
      email,
      password,
    });

    const u = response.data;

    setUser(u);
    localStorage.setItem("civanta_user", JSON.stringify(u));

    return u;
  };

  const register = async (data) => {
    const response = await authService.register({
      name: data.name,
      email: data.email,
      password: data.password,
      language: data.language || "en",
    });

    const u = response.data;

    setUser(u);
    localStorage.setItem("civanta_user", JSON.stringify(u));

    return u;
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("civanta_user");
    localStorage.removeItem("civanta_token");
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        login,
        register,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
