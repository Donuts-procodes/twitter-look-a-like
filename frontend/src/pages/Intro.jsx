import { Link } from 'react-router-dom';

export default function Intro() {
  return (
    <div>
      <h1>Welcome to Our App</h1>
      <Link to="/register"><button>Register</button></Link>
      <Link to="/login"><button>Login</button></Link>
    </div>
  );
}
