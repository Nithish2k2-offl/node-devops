import { useEffect, useState } from 'react';
import './App.css';

// localStorage.clear();
// sessionStorage.clear();

const defaultTasks = [
  'Do Exercise',
  'Have Breakfast',
  'Read Books',
  'Have Coffee'
];

function App() {
  const [tasks, setTasks] = useState([]);
  const [taskInput, setTaskInput] = useState('');

  useEffect(() => {
    const storedTasks = localStorage.getItem('tasks');

    if (storedTasks) {
      setTasks(JSON.parse(storedTasks));
    } else {
      setTasks(defaultTasks);
      localStorage.setItem('tasks', JSON.stringify(defaultTasks));
    }
  }, []);

  function createTask() {
    const task = taskInput.trim();

    if (!task) return;

    const updatedTasks = [...tasks, task];

    setTasks(updatedTasks);
    localStorage.setItem('tasks', JSON.stringify(updatedTasks));
    setTaskInput('');
  }

  return (
    <div className="container">
      <div className="box">
        <h2>Container To-Do List</h2>

        <div className="input-row">
          <input
            type="text"
            value={taskInput}
            onChange={(e) => setTaskInput(e.target.value)}
            placeholder="Enter a new task..."
            onKeyDown={(e) => {
              if (e.key === 'Enter') {
                createTask();
              }
            }}
          />

          <button onClick={createTask}>
            Create
          </button>
        </div>

        <ul>
          {tasks.map((task, index) => (
            <li key={index}>{task}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;