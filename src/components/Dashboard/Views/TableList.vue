<template>
    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <div class="col-md-12">
            <div class="col-md-3 pull-right">
              <p class="category">To :</p>
               <input type="date" v-model="listQuery.toDate" @change="getList()"/>
               <input type="time" v-model="listQuery.toTime"  @change="getList()"/>
            </div>  
            <div class="col-md-3 pull-right">
              <p class="category">From : </p>
               <input type="date" v-model="listQuery.fromDate"  @change="getList()"/>
               <input type="time" v-model="listQuery.fromTime"  @change="getList()"/>
            </div>
          </div>
          <paper-table :title="table1.title" :sub-title="table1.subTitle" :data="table1.data" :columns="table1.columns">

          </paper-table>
        </div>
      </div>
    </div>
</template>
<script>
  import PaperTable from 'components/UIComponents/PaperTable.vue'
  import { fetchList } from '../../../api/objects'
  const tableColumns = ['ObjectType', 'Accurency', 'Time']

  export default {
    components: {
      PaperTable
    },
    data () {
      return {
        table1: {
          title: 'Detected Objects',
          subTitle: '',
          columns: [...tableColumns],
          data: []
        },
        listQuery: {
          fromDate: null,
          fromTime: null,
          toDate: null,
          toTime: null
        }
      }
    },
    created () {
      var now = new Date()
      var month = (now.getMonth() + 1)
      var day = now.getDate()
      if (month < 10) {
        month = '0' + month
      }
      if (day < 10) {
        day = '0' + day
      }
      var today = now.getFullYear() + '-' + month + '-' + day
      this.fromDate = today
      this.getList()
    },
    methods: {
      getList () {
        fetchList(this.listQuery).then(response => {
          console.log(JSON.parse(response.data)[0])
          this.table1.data = JSON.parse(response.data)
        })
      }
    }
  }

</script>
<style>

</style>
