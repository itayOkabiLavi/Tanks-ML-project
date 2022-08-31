import logo from './logo.svg';
import './App.css';
import TrainingZone from './components/TrainingZone';

function App() {
  return (
    <div className="App">
      <div id='menu'>
      Menu
      </div>
      <div id='main'>
        <TrainingZone/>
      </div>
    </div>
  );
}

export default App;
