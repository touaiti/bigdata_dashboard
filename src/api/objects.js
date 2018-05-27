import request from '../utils/request'

export function fetchList (query) {
  return request({
    url: '/objects/list',
    method: 'get',
    params: query
  })
}

export function fetchStatistics (query) {
  return request({
    url: '/objects/statistics',
    method: 'get',
    params: query
  })
}
