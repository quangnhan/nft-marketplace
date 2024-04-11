import httpService from "./httpService";

const API_ENDPOINT = `${process.env.REACT_APP_SERVER_URL}/api/token/`;
const TOKEN = "token";
const USER_INFO = "userInfo";

httpService.setJwt(getToken());

async function login(username: string, password: string) {
  const { data } = await httpService.post(API_ENDPOINT, { username, password });
  localStorage.setItem(TOKEN, data.key);
  localStorage.setItem(USER_INFO, JSON.stringify({ username }));
  httpService.setJwt(getToken());
}

function logout() {
  localStorage.clear();
}

function getToken(): string | null {
  return localStorage.getItem(TOKEN);
}

function getCurrentUser() {
  const userString = localStorage.getItem(USER_INFO);
  if (userString !== null) {
    const user = JSON.parse(userString);
    return user;
  }
  return null;
}

const authService = {
  login,
  logout,
  getToken,
  getCurrentUser,
};

export default authService;
