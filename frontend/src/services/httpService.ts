import axios from "axios";

axios.interceptors.response.use(null, (error) => {
  const exepctedError =
    error.response &&
    error.response.status >= 400 &&
    error.response.status < 500;

  if (!exepctedError) {
    console.error("Something go wrong!!");
  }

  // Check if the response status is 428 (Precondition Required)
  if (error.response && error.response.status === 428) {
  }

  return Promise.reject(error);
});

// Set the AUTH token for any request
function setJwt(jwt: string | null) {
  axios.defaults.headers.common["Authorization"] = jwt ? `Token ${jwt}` : "";
}

const httpService = {
  get: axios.get,
  post: axios.post,
  put: axios.put,
  delete: axios.delete,
  setJwt: setJwt,
};

export default httpService;
