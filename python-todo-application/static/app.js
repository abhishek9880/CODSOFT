$(document).ready(function () {
  const taskInput = $("#taskInput");
  const addTaskBtn = $("#addTaskBtn");
  const taskList = $("#taskList");

  addTaskBtn.click(function () {
    const taskText = taskInput.val().trim();
    if (taskText !== "") {
      $.ajax({
        type: "POST",
        url: "/add",
        contentType: "application/json",
        data: JSON.stringify({ description: taskText }),
        success: function (data) {
          window.location.reload();
        },
      });
    }
  });

  taskList.on("click", ".edit", function () {
    const taskItem = $(this).closest(".list-group-item");
    const taskId = taskItem.find("span").attr("id");
    const currentDescription = taskItem.find("span").text();
    const newTaskText = prompt("Edit task:", currentDescription);
    if (newTaskText !== null) {
      $.ajax({
        type: "PUT",
        url: `/edit/${taskId}`,
        contentType: "application/json",
        data: JSON.stringify({ description: newTaskText }),
        success: function (data) {
          taskItem.find("span").text(data.description);
        },
      });
    }
  });

  taskList.on("click", ".delete", function () {
    const taskItem = $(this).closest(".list-group-item");
    const taskId = taskItem.find("span").attr("id");
    $.ajax({
      type: "DELETE",
      url: `/delete/${taskId}`,
      success: function () {
        taskItem.remove();
      },
    });
  });
});
