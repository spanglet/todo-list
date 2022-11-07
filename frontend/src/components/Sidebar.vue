<template>
  <!-- Sidebar allows changes to the user's view of lists/calendars -->
  <div class="sidebar">

    <SidebarTile
      name="Lists"
      @clicked="store.deleteList"
      path='todo/'
      :routes="store.lists"
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

<script setup>

  import SidebarTile from "./SidebarTile.vue"
  import ListForm from "./ListForm.vue"
  import SymbolButton from "./SymbolButton.vue"
  import { useLists } from '../stores/lists.js'

  const store = useLists()

  const calendarRoutes = [
    { name: "Month",
      id: "month"
    },
    { name: "Week",
      id: "week"
    },
  ]
  const icons = ["xmark"]

</script>

<style>

  .sidebar {
    display: flex;
    color: white;
    flex-flow: column nowrap;
    align-items: stretch;
    gap: 3px;
  }

</style>

