<template>
  <div>

    <!--Stats cards-->
    <div class="row col-md-12 text-center">
        <img src="static/img/bd.png" alt="" style="width:60%">
    </div>
    <div class="row">
      <div class="col-lg-3 col-sm-6">
        <stats-card>
          <div class="icon-big text-center" :class="`icon-warning`" slot="header">
            <i class="ti-server"></i>
          </div>
          <div class="numbers" slot="content">
            <p>Number of Objects</p>
            {{nbObjects}}
          </div>
          <div class="stats" slot="footer">
            <i class="ti-reload"></i> Updated now
          </div>
        </stats-card>
      </div>
      <div class="col-lg-3 col-sm-6">
        <stats-card>
          <div class="icon-big text-center" :class="`icon-success`" slot="header">
            <i class="ti-user"></i>
          </div>
          <div class="numbers" slot="content">
            <p>Number Of Persons</p>
            {{nbPerson}}
          </div>
          <div class="stats" slot="footer">
            <i class="ti-calendar"></i> Last Day
          </div>
        </stats-card>
      </div>
    </div>

    <!--Charts-->
    <div class="row">
      <!--
      <div class="col-xs-12">
        <chart-card :chart-data="usersChart.data" :chart-options="usersChart.options">
          <h4 class="title" slot="title">Objects detected per hour</h4>
          <span slot="subTitle"> 24 Hours performance</span>
          <span slot="footer">
            <i class="ti-reload"></i> Updated 3 minutes ago</span>
          <div slot="legend">
            <i class="fa fa-circle text-info"></i> Open
            <i class="fa fa-circle text-danger"></i> Click
            <i class="fa fa-circle text-warning"></i> Click Second Time
          </div>
        </chart-card>
      </div>
      <div class="col-md-6 col-xs-12">
        <chart-card :chart-data="preferencesChart.data"  chart-type="Pie">
          <h4 class="title" slot="title">Email Statistics</h4>
          <span slot="subTitle"> Last campaign performance</span>
          <span slot="footer">
            <i class="ti-timer"></i> Campaign set 2 days ago</span>
          <div slot="legend">
            <i class="fa fa-circle text-info"></i> Open
            <i class="fa fa-circle text-danger"></i> Bounce
            <i class="fa fa-circle text-warning"></i> Unsubscribe
          </div>
        </chart-card>
      </div>
      -->
      <div class="col-md-12 col-xs-12 card container">
         <div class="col-md-3 pull-right">
              <p class="category">
                <br/>
                Date :
                <input type="date" v-model="listQuery.date" />
              </p>
               
        </div>
      <div class="col-md-12 col-xs-12 ">
          
        
        <chart-card v-if="showGrid" :chart-data="activityChart.data" :chart-options="activityChart.options">
          <h4 class="title" slot="title">Objects detected per hour</h4>

          <span slot="subTitle"> 24 Hours performance</span>
          <span slot="footer">
            <i class="ti-reload"></i> Updated 1 minutes ago</span>
          <div slot="legend">
            
            <i class="fa fa-circle text-info"></i> Objects
          </div>
        </chart-card>
      </div>

    </div>
    </div>
  </div>
</template>
<script>
  import StatsCard from 'components/UIComponents/Cards/StatsCard.vue'
  import ChartCard from 'components/UIComponents/Cards/ChartCard.vue'
  import { fetchList, fetchStatistics } from '../../../api/objects'
  export default {
    components: {
      StatsCard,
      ChartCard
    },
    /**
     * Chart data used to render stats, charts. Should be replaced with server data
     */
    data () {
      return {
        nbPerson: 0,
        nbObjects: 0,
        showGrid: false,
        listQuery: {
          date: null
        },
        /*
        usersChart: {
          data: {
            labels: ['9:00AM', '12:00AM', '3:00PM', '6:00PM', '9:00PM', '12:00PM', '3:00AM', '6:00AM'],
            series: [
              [287, 385, 490, 562, 594, 626, 698, 895, 952],
              [67, 152, 193, 240, 387, 435, 535, 642, 744],
              [23, 113, 67, 108, 190, 239, 307, 410, 410]
            ]
          },
          options: {
            low: 0,
            high: 1000,
            showArea: true,
            height: '245px',
            axisX: {
              showGrid: false
            },
            lineSmooth: this.$Chartist.Interpolation.simple({
              divisor: 3
            }),
            showLine: true,
            showPoint: false
          }
        },
         */
        activityChart: {
          data: {
            labels: ['6:00AM', '7:00AM', '8:00AM', '9:00AM', '10:00AM', '11:00AM', '12:00AM', '01:00PM', '02:00PM', '03:00PM', '04:00PM', '05:00PM', '06:00PM', '07:00PM', '08:00PM'],
            series: [
              [230, 293, 380, 480, 503, 553, 600, 664, 698, 710, 736, 795, 664, 698, 710]
            ]
          },
          options: {
            seriesBarDistance: 10,
            axisX: {
              showGrid: true
            },
            height: '270px'
          }
        },
        preferencesChart: {
          data: {
            labels: ['62%', '32%', '6%'],
            series: [62, 32, 6]
          },
          options: {}
        }

      }
    },
    mounted () {
      let d = []
      fetchList(this.listQuery).then(reponse => {
        reponse.data.items.forEach(element => {
          d.push(Number(element.total))
        })
        this.activityChart.data.series = [d]
        this.showGrid = true
      })
      fetchStatistics().then(reponse => {
        this.nbPerson = reponse.data.nbPerson
        this.nbObjects = reponse.data.nbObjects
      })
    }
  }
</script>
<style>

</style>
