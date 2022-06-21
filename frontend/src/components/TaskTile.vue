<template> 
  <div class="tile">
    <div class="col">
      <div>{{name}}</div>
    </div>  
    <div class="col">
      <div>{{description}}</div>
    </div>  
    <div class="col">
      <div>{{formattedDueDate}}</div>
    </div>  
    <Button class="tile-button del-button" :action="removeItem"  btn-type="xmark" />
    <Button class="tile-button done-button" :action="markTaskCompleted" btn-type="check" />
  </div>
</template>


<script>

  import Button from "./Button.vue"
  
  var days = ['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']
  var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
      "Jul","Aug", "Sep", "Oct", "Nov", "Dec"]

  export default { 
    components: {
      Button
    },
    data() {
      return {
      }
    },
    emits: ['removeItem'],
    props: {
      name: String,
      description: String,
      dueDate: String
    },
    methods: {
      // Emit delete event to App parent container
      removeItem() {
        this.$emit('removeItem')
      },
      markTaskCompleted() {
        this.$emit('taskCompleted')
      }
    },
    computed: {
  
      formattedDueDate() {
        var date = new Date(this.dueDate)
        return days[date.getDay()] + ", " +
            months[date.getMonth()] + " " +
            date.getDate() 
      }
    }
  }
</script>


<style>

  .tile {
    display: flex;
    align-items: stretch;
    justify-content: center;
    margin: 0;
    list-style: none;
    border: 2px #b378cc outset;
    border-radius: 8px;
    background: #bb8fce;
    gap: 5px;
    height: 40px;
  }
  .col {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1em;
    font-size: 20px;
    flex: 1;
  }
  .tile-button {
    margin: 2px; 
    width: 4%;
  }
  .del-button {
    background: darksalmon;
  }
  .done-button {
    background: lightgreen;
  }

</style>
