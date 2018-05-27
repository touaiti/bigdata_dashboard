<template>
    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <div class="col-md-12">
            <div class="col-md-3 pull-right">
              <p class="category">To :</p>
               <input type="date" v-model="listQuery.toDate" />
               <input type="time" v-model="listQuery.toTime"/>
            </div>  
            <div class="col-md-3 pull-right">
              <p class="category">From : </p>
               <input type="date" v-model="listQuery.fromDate"/>
               <input type="time" v-model="listQuery.fromTime"/>
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
  const tableColumns = ['type', 'total', 'time']

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
      fetchList(this.listQuery).then(response => {
        this.table1.data = response.data.items
      })
    }
  }

</script>
<style>

</style>
