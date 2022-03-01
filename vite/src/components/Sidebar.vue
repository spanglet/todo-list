<!-- Sidebar.vue -->

<template>

  <div class="sidebar">
    <div>Lists</div>
    <div>Calendar</div>
    <div>Other</div>
  </div>

</template>


<script>

  export default {
    data() {
      return {
     
      }
    }
  }

</script>


<style>

  .sidebar {
    display: flex;
    background: hsl(var(--hue-purple),100%,var(--lgt-3));
    flex-flow: column;
    justify-content: flex-start;
    align-items: center;
    color: white;
    
  }
  
  .sidebar > * {
    font-size: 16pt;
    padding: 10px;
  }

</style>

