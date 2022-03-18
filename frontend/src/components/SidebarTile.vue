
<template>

  <div class="sidebar-tile">

    <div class="sidebar-tile-header" @click="expand">
      {{ text }}
      <Button class="form-btn" :btn-type="expandIcon" @click="this.$emit('viewForm')" />
    </div>

    <div class="expanded-content" v-if="expanded" v-for="list in lists">
      <div @click="changeList(list.id)"> {{ list.name }}</div>
    </div>
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
        expanded: false,
        expandIcon: "plus",
      }
    },
    props: ["lists", "text"],
    emits: ['viewForm','listChanged'],
    methods: {
      // Expand or shrink when title is clicked
      expand: function () {
        this.expanded = !this.expanded
      },
      // Emit the list change to the root (App) component for handling
      changeList: function(list) {
        this.$emit('listChanged', list)
      }
    }
  }

</script>


<style>

  .sidebar-tile {
    display: flex;
    flex-flow: column nowrap;
    align-items: center;
  }

  .sidebar-tile-header {
    display: flex;
    font-size: 20pt;
    justify-content: space-between;
    height: 50px;
    gap: 60px;
    margin: 10px;
  }
  .expanded-content {
    font-size: 16pt;
  }
  .expanded-content:hover {
    background-color: grey;
  }
  

</style>

