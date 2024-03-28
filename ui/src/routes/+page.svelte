<script>
import axios from 'axios';

let url = '';
let score = 0;
let checked = false;
async function checkUrl() {
    const response = await axios.post('http://localhost:5000/check_url', { url });
    console.log(response.data.score);
    checked = true;
    score += response.data.score;
}
</script>

<div class="flex flex-col space-y-10 justify-center items-center">
  <p class="text-2xl"><span class="text-green-600">Fraud Detection: </span><span class="text-violet-500"> Detect and Prevent Fraud</span></p>

  <div class="flex flex-row space-x-4">
    <input bind:value={url} type="text" class="input input-bordered w-full max-w-xs" placeholder="enter the url">
    <button on:click={checkUrl} class="btn btn-outline btn-accent">Check</button>
  </div>
  {#if checked}
  <p class="text-xl"><span>Score:</span>{score}</p>
    {/if}
</div>


<!-- <input bind:value={url} type="text" placeholder="Enter URL">
<button on:click={checkUrl}>Check</button> -->