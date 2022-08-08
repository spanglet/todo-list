<template>
  <!-- Sidebar allows changes to the user's view of lists/calendars -->
  <div class="sidebar">

    <SidebarTile
      text="Lists"
      path='todo/'
      :routes="currentLists"
      @list-removed="removeList"
      @list-changed="changeList"
    >

      <ListForm />

    </SidebarTile>

    <SidebarTile
      text="Calendar"
      path="calendar/"
      :routes="calendarRoutes"
    />

  </div>
</template>

<script>

  import SidebarTile from "./SidebarTile.vue"
  import ListForm from "./ListForm.vue"

  export default {
    components: {
      SidebarTile,
      ListForm,
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
        ]
      }
    },
    methods: {
      changeList: function (list) {
        /* Change current list view at App component
         */
        this.$emit("listChanged", list)
      },
      removeList: function (list) {
        /* Send delete request for list to backend
         */
        this.axios.delete("lists/" + String(list.id))
          .then((res) => {
            if (res.status == 200) {
              this.$emit("notification",list.name)
            }
          })
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
  .list-form {
    display: flex;
    flex-flow: column nowrap;
    justify-content: center;
    align-items: stretch;
    gap: .5em;
    margin: 3px;
  }
  .list-form input {
    font-size: 18pt;
  }

</style>

