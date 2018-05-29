import request from '../utils/request'

export function fetchList (query) {
  return request({
    url: 'http://127.0.0.1:5000/objects',
    method: 'get',
    params: query
  })
}

export function fetchStatistics (query) {
  return request({
    url: 'http://127.0.0.1:5000/objects/statistics',
    method: 'get',
    params: query
  })
}

export function fetchPercent (query) {
  return request({
    url: 'http://127.0.0.1:5000/objects/percents',
    method: 'get',
    params: query
  })
}
