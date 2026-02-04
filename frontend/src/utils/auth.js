export function saveUser(userId) {
  localStorage.setItem("user_id", userId);
}

export function getUser() {
  return localStorage.getItem("user_id");
}

export function logout() {
  localStorage.removeItem("user_id");
}
