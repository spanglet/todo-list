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
    <Button class="del-button" :action="removeItem"  btn-type="xmark" />
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
      dueDate: Date
    },
    methods: {
      // Emit delete event to App parent container
      removeItem() {
        this.$emit('removeItem')
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
    border-radius: 8px;
    background:  #bb8fce;
    gap: 5px;
    height: 40px;
  }
  .col {
    text-align: center;
    padding: 1em;
    margin: auto;
    font-size: 20px;
    flex: 1;
  }
  .del-button {
    margin: 2px; 
    background: darksalmon;
    width: 5%;
  }
  

</style>
