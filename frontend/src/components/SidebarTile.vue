
<template>

  <div class="sidebar-tile">

    <div class="sidebar-tile-header sidebar-tile-item" @click="expand">
      {{ text }}
      <font-awesome-icon :icon="dropdownIcon" /> 
    </div>

    <TransitionGroup>
      <div class="sidebar-expanded-group" v-if="expanded">

        <div 
          class="sidebar-expanded-item sidebar-tile-item"
          v-for="route in routes"
          :key="route.id"
          :class="{ 'active-route': isActiveRoute(route.id) }"
          @click="routeTo(route.id)"
        >
          {{ route.name }}
        </div>

        <slot name="footer-slot"/>
      </div>
    </TransitionGroup>

  </div>

</template>


<script>

  import { useTasks } from '../stores/tasks.js'

  export default {
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    components: {
       
    },
    props: ["text","path","routes"],
    data() {
      return {
        expanded: false,
      }
    },
    computed: {
      dropdownIcon() {
        return this.expanded ? 'angle-up' : 'angle-down'
      },
      basePath() {
        return '/app/' + this.path
      },
    },
    methods: {
      // Expand or shrink when title is clicked
      expand() {
        this.expanded = !this.expanded
      },
      // Emit the list change to the root (App) component for handling
      routeTo(id) {
        this.$router.push(this.basePath + id.toString() )
      },
      isActiveRoute (id) {
        return this.$route.path === (this.basePath + id)
      },
    }
  }

</script>


<style>

  .sidebar-tile {
    display: flex;
    flex-flow: column nowrap;
    align-items: stretch;
    gap: 10px;
  }
  .sidebar-tile-header {
    display: flex;
    font-size: 1.75em;
    justify-content: space-between;
    align-items: center;
    height: 30px;
    box-shadow: 0px 3px 5px 1px black;
    padding: 5px;
  }
  .sidebar-expanded-group {
    display: flex;
    flex-flow: column nowrap;
    gap: 5px;
  }
  .sidebar-expanded-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 25px;
    font-size: 16pt;
    border-radius: 2px;
    text-align: left;
    flex: 1;
    padding: 5px;
    border-bottom: 1px solid #3c0e97;
  }
  .v-enter-active,
  .v-leave-active {
    transition: all .5s ease;
  }
  .v-leave-to,
  .v-enter-from {
    opacity: 0;
  }
  .active-route {
    background-color: hsl(var(--hue-purple),100%,var(--lgt-2));
  }
  .sidebar-tile-item:hover {
    background: hsl(var(--hue-purple),100%,var(--lgt-2));
  }

</style>

