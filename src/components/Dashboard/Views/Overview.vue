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
      <div class="col-lg-3 col-sm-6" v-for="o in objects">
        <stats-card>
          <div class="icon-big text-center" :class="`icon-success`" slot="header">
            <i :class="[o._id === 'cell phone' ? 'ti-mobile' : o._id === 'person' ? 'ti-user' : '', 'ti-sever']"></i>
          </div>
          <div class="numbers" slot="content">
            <p>Number Of {{o._id}}</p>
            {{o.count}}
          </div>
          <div class="stats" slot="footer">
            <i class="ti-reload"></i> Updated now
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
      -->
      <div class="col-md-6 col-xs-12">
        <chart-card  v-if="pieChart" :chart-data="preferencesChart.data"  chart-type="Pie">
          <h4 class="title" slot="title">Objects Statistics</h4>
          <span slot="subTitle"> Types performance</span>
          <span slot="footer">
            <i class="ti-reload"></i> Updated Now</span>
          <div slot="legend">
            <span v-for=" t in types">
                <i  :class="'fa fa-circle text-' + t.color"></i> {{t.text}}
            </span>
          </div>
        </chart-card>
      </div>
      <div class="col-md-12 col-xs-12 card container" style="heigth: 550px">
         <div class="col-md-3 pull-right">
              <p class="category">
                <br/>
                Date :
                <input type="date" v-model="listQuery.date" @change="getStatistics()" />
              </p>
        </div>
      <div class="col-md-12 col-xs-12 ">
        <chart-card v-if="showGrid" :chart-data="activityChart.data" :chart-options="activityChart.options">
          <h4 class="title" slot="title">Objects detected per hour</h4>

          <span slot="subTitle"> 24 Hours performance</span>
          <span slot="footer">
            <i class="ti-reload"></i> Updated now</span>
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
  import { fetchStatistics, fetchPercent } from '../../../api/objects'
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
        nbPersons: 0,
        nbObjects: 0,
        showGrid: false,
        pieChart: false,
        listQuery: {
          date: null
        },
        colors: ['info', 'warning', 'danger', 'success'],
        types: [],
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
            labels: ['00AM', '01AM', '02AM', '03AM', '04AM', '05AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12AM', '01PM', '02PM', '03PM', '04PM', '05PM', '06PM', '07PM', '08PM', '09PM', '10PM', '11PM'],
            series: [
              []
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
      this.getStatistics()
      this.getPercents()
    },
    methods: {
      getStatistics () {
        this.showGrid = false
        fetchStatistics(this.listQuery).then(reponse => {
          var i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
          var s = []
          var data = JSON.parse(reponse.data)
          i.forEach(element => {
            var d = data.find((d) => { return Number(d._id) === element })
            if (d) {
              s.push(d.count)
            } else {
              s.push(0)
            }
          })
          this.activityChart.data.series = [s]
          this.showGrid = true
        })
      },
      getPercents () {
        fetchPercent().then(reponse => {
          var data = JSON.parse(reponse.data)
          this.pieChart = false
          var l = []
          var s = []
          var index = 0
          this.objects = data
          data.forEach(element => {
            if (!isNaN(element.count)) {
              this.nbObjects += element.count
            }
            if (element._id === 'person') {
              this.nbPersons += element.count
            }
            l.push(Number(element.percent) * 100 + '%')
            s.push(Number(element.percent))
            this.types.push({color: this.colors[index++], text: element._id})
          })
          this.preferencesChart.data.labels = l
          this.preferencesChart.data.series = s
          this.pieChart = true
        })
      }
    }
  }
</script>
<style>

</style>
