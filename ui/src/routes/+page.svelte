<script>
import axios from 'axios';

let url = '';
let score = 0;
let checked = false;
async function checkUrl() {
    const response = await axios.post('http://localhost:5000/check_url', { url });
    score = 0
    console.log(response.data.score);
    checked = true;
    score += response.data.score;
}
let scoreColor = "text-red";
$: if(score > 85){
  scoreColor = "text-green-600";
} else if(score > 70){
  scoreColor = "text-yellow-500";
} else if(score > 50){
  scoreColor = "text-amber-700";
} else {
  scoreColor = "text-red-500";
}
</script>

<div class="flex flex-col my-48 space-y-8 justify-center items-center font-mono">
  <p class="text-2xl"><span class="text-green-600">Secure Guardian: </span><span class="text-violet-500"> Detect and Prevent Fraud</span></p>

  <div class="flex flex-col space-y-2">
    <div class="flex flex-row space-x-4">
      <input bind:value={url} type="text" class="input input-bordered w-full max-w-xs" placeholder="enter the url">
      <button on:click={checkUrl} class="btn btn-outline btn-accent">Check</button>
    </div>
    <p class="text-sm bg-gray-50 bg-opacity-30 px-1 rounded-lg">please enter the url in http(s)://www.example.com format</p>
  </div>

  {#if checked}
  <div class="flex flex-col space-y-1">
    <p class="text-xl"><span>Trustability Score:</span><span class={scoreColor}>{score}</span>/100</p>
    <p class="text-center">
      {#if score > 85}
      <span class="text-green-600">This website is safe to visit!</span>
      {:else if score > 70}
      <span class="text-yellow-500">This website is safe to visit!</span>
      {:else if score > 50}
      <span class="text-amber-700">This website is doesn't seem safe, please be careful.</span>
      {:else}
      <span class="text-red-500">This website is definately not safe to visit, Avoid this website!</span>
      {/if}
    </p>
  </div>
  {/if}
</div>