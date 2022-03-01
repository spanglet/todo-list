<template> 
  <div class=tile>
    <div class="col">
      <div>{{name}}</div>
    </div>  
    <div class="col">
      <div>{{description}}</div>
    </div>  
    <Button class="del-button" :action="removeItem"  icon="xmark" />
  </div>
</template>


<script>

  import Button from "./Button.vue"

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
      description: String
    },
    methods: {
      // Emit delete event to App parent container
      removeItem() {
        this.$emit('removeItem')
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
  }
  .del-button {
    margin: 2px; 
    background: darksalmon;
    width: 10%;
  }
  

</style>
