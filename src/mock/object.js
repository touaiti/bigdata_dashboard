import Mock from 'mockjs'
import { param2Obj } from '../utils'

const List = []
const count = 15

for (let i = 0; i < count; i++) {
  List.push(Mock.mock({
    id: '@increment',
    type: 'Person',
    total: '152',
    time: '16:12'
  }))
}

export default {
  getList: config => {
    const { importance, type, title, page = 1, limit = 20, sort } = param2Obj(config.url)

    let mockList = List.filter(item => {
      if (importance && item.importance !== +importance) return false
      if (type && item.type !== type) return false
      if (title && item.title.indexOf(title) < 0) return false
      return true
    })

    if (sort === '-id') {
      mockList = mockList.reverse()
    }

    const pageList = mockList.filter((item, index) => index < limit * page && index >= limit * (page - 1))

    return {
      total: mockList.length,
      items: pageList
    }
  },

  getObject: () => ({
    id: 120000000001,
    type: 'Person',
    total: '152',
    time: '16:12'
  })
}
