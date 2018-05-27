import Mock from 'mockjs'
import objectAPI from './object'

// Mock.setup({
//   timeout: '350-600'
// })

Mock.mock(/\/objects\/list/, 'get', objectAPI.getList)

export default Mock
