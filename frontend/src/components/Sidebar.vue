<template>
  <!-- Sidebar allows changes to the user's view of lists/calendars -->
  <div class="sidebar">

    <SidebarTile
      name="Lists"
      @clicked="removeList"
      path='todo/'
      :routes="currentLists"
      footer
      tile-button
    >

      <template #sidebar-tile-button>
        <SymbolButton
          :icons="icons"
        />
      </template>

      <template #sidebar-tile-footer>
        <ListForm />
      </template>

    </SidebarTile>

    <SidebarTile
      name="Calendar"
      path="calendar/"
      :routes="calendarRoutes"
    />

    <SidebarTile
      name="Completed Tasks"
      path="todo/completed"
    />

  </div>
</template>

<script>

  import SidebarTile from "./SidebarTile.vue"
  import ListForm from "./ListForm.vue"
  import SymbolButton from "./SymbolButton.vue"
  import { useLists } from '../stores/lists.js'

  export default {
    setup() {
      const store = useLists()
      return {
        store,
      }
    },
    components: {
      ListForm,
      SidebarTile,
      SymbolButton,
    },
    inject: ['currentLists'],
    emits: [
      'listChanged',
      'listsUpdated',
      'notification',
    ],
    data() {
      return {
        calendarRoutes: [
          { name: "Month",
            id: "month"
          },
          { name: "Week",
            id: "week"
          },
        ],
        icons: ["xmark"]
      }
    },
    methods: {
      removeList: function (list_id) {
        /* Send delete request for list to backend
         */
        this.store.deleteList(list_id)
      },
    }      
  }

</script>

<style>

  .sidebar {
    display: flex;
    background: hsl(var(--hue-purple),100%,var(--lgt-3));
    color: white;
    flex-flow: column nowrap;
    align-items: stretch;
    margin: 8px;
    gap: 3px;
  }

</style>

