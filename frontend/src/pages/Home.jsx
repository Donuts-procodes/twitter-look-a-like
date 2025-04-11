import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';

export default function Home() {
  const navigate = useNavigate();
  const user = localStorage.getItem('user');

  useEffect(() => {
    if (!user) navigate('/intro');
  }, [navigate, user]);

  const logout = () => {
    localStorage.removeItem('user');
    navigate('/intro');
  };

  return (
    <div>
      <h2>Welcome, {user}</h2>
      <button onClick={logout}>Logout</button>
    </div>
  );
}
