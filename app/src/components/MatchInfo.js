import React from "react";
import { useSelector } from "react-redux";

function MatchInfo({ playerList }) {
  const game = useSelector((state) => state.match);
  const user = useSelector((state) => state.user);

  const startGame = async () => {
    const url = "http://127.0.0.1:8000";

    await fetch(url + "/game/" + game.id + "?user=" + user.id, {
      method: "PATCH",
    })
      .then((response) => {
        console.log(response);
        if (response.status !== 200) {
          if (response.status === 404) {
            alert("Unable to start");
          } else {
            alert("Unknown error");
          }
        } else {
        }
      })
      .catch(() => {
        alert("Network Error");
      });
  };

  return (
    <div>
      {user.id === game.hostId ? (
        <div>
          <h3>You are the host</h3>
          <button
            onClick={() => {
              startGame();
            }}
          >
            Start Game
          </button>
        </div>
      ) : (
        <h3>Waiting for Host to start the game</h3>
      )}
      <h1>Players joined:</h1>
      {Object.entries(playerList).map((player) => (
        <h4>{player[0]}</h4>
      ))}
    </div>
  );
}
export default MatchInfo;
