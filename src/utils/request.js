import axios from 'axios'

// create an axios instance
const service = axios.create({
  baseURL: process.env.BASE_API, // api base_url
  timeout: 5000 // request timeout
})

// request interceptor
service.interceptors.request.use(config => {
  // Do something before request is sent

  config.headers['Content-Type'] = 'application/json'

  return config
}, error => {
  // Do something with request error
  console.log('error request' + error)
  Promise.reject(error)
})

// respone interceptor
service.interceptors.response.use(
  response => response,
  error => {
    console.log('err' + error)
    return Promise.reject(error)
  })

export default service
