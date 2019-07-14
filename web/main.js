let data;

async function get_sensor_data() {
  data = await eel.all()();
  console.log(data);
}

function print_test() {
  console.log(data);
}
