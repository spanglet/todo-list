
<template>

  <div class="sidebar-tile">

    <div class="sidebar-tile-header" @click="expand">
      {{ text }}
      <font-awesome-icon :icon="dropdownIcon" /> 
    </div>

    <TransitionGroup>
      <div class="sidebar-expanded-group" v-if="expanded">

        <div 
          class="sidebar-expanded-item"
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
    },
    methods: {
      // Expand or shrink when title is clicked
      expand() {
        this.expanded = !this.expanded
      },
      // Emit the list change to the root (App) component for handling
      isActiveRoute (route) {
        return false
      },
      routeTo(id) {
        this.$router.push("/app/" + this.path + id.toString() )
      }
    }
  }

</script>


<style>

  .sidebar-tile {
    display: flex;
    flex-flow: column nowrap;
    align-items: stretch;
    margin: 5px;
    gap: 10px;
  }
  .sidebar-tile-header {
    display: flex;
    font-size: 1.8em;
    justify-content: space-between;
    height: 30px;
    box-shadow: 0px 3px 9px -8px black;
    padding: 5px;
  }
  .sidebar-tile-header:hover {
    background: hsl(var(--hue-purple),100%,var(--lgt-2));
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
    text-align: left;
    flex: 1;
  }
  .v-enter-active,
  .v-leave-active {
    transition: all .5s ease;
  }
  .v-leave-to,
  .v-enter-from {
    opacity: 0;
  }
  .expanded-content:hover {
    background-color: grey;
  }
  .active-list {
    background-color: hsl(var(--hue-purple),100%,var(--lgt-2));
  }

</style>

