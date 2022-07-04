<template>

 <div>
  <div class="list-header">
    <div class="col-header"> Name </div>
    <div class="col-header"> Description </div>
    <div class="col-header"> Due Date </div>
    <Button class="plus-button" :btn-type="buttonIcon" :action="changeFormVisibility" />
  </div>
 </div>

</template>


<script>

  import Button from "./Button.vue"
  import { useTasks } from "../stores/tasks.js"

  export default { 

    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    components: {
      Button
    },
    //emits: ['formVisible'],
    data() {
      return {
        name: "",
        description: "",
        tasks: {},
      }
    },
    methods: { 
      // triggered on successful form submission
      // emits event up to main container for list refresh
      changeFormVisibility() {
        this.store.taskFormActive = !this.store.taskFormActive
      }
    },
    computed: {
      buttonIcon() {     
        /**  Icon is minus ( - ) if form expanded ( + ) if inactive */
        return (this.store.taskFormActive ? "minus" : "plus")
      }
    }
  }

</script>


<style>

  .list-header {
    display: flex;
    list-style: none;
    justify-content:center;
    align-items: stretch;
    color: white;
    font-size: 20px;
    margin: .4em;
    border-radius: 8px;
    border: 1px solid black;
    background: hsl(var(--hue-purple), 100%, var(--lgt-4 ));
    box-shadow: 0 4px 8px -7px black;
  }
  .col-header {
    display: flex;
    flex: 5;
    text-align: center;
    align-items: center;
    justify-content: center;
    border-left: 2px solid black;
  }
  .plus-button {
    display: flex;
    flex: 1;
    background: hsl(var(--hue-green), 100%, var(--lgt-3));
  }

</style>
