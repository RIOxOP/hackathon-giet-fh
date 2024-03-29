<script>
  import axios from "axios";
  import Info from "../lib/info.svelte";
  import { fade } from "svelte/transition";

  let url = "";
  let score = 0;
  let checked = false;
  async function checkUrl() {
    const response = await axios.post("http://localhost:5000/check_url", {
      url,
    });
    score = 0;
    console.log(response.data.score);
    checked = true;
    score += response.data.score;
  }
  let scoreColor = "text-red";
  $: if (score > 85) {
    scoreColor = "text-green-600";
  } else if (score > 70) {
    scoreColor = "text-yellow-500";
  } else if (score > 50) {
    scoreColor = "text-amber-700";
  } else {
    scoreColor = "text-red-500";
  }
</script>

<div class="flex flex-col space-y-6 justify-center items-center font-mono mx-8">
  <h1 class="text-2xl text-success font-bold">
    Check a URL's Trustworthiness in Seconds :)
  </h1>
  <h3>
    Do you know there are <span class="text-error">100,000</span> peoples are
    falling for scams everyday?
    <span class="text-success"> Don't get phished! </span> Paste any website and
    get a real-time fraud score. Know before you click with our powerful URL analysis
    tool.
  </h3>
  <div class="flex flex-col space-y-2">
    <div class="flex flex-row space-x-4">
      <input
        bind:value={url}
        type="text"
        class="input input-bordered w-full max-w-xs"
        placeholder="enter the url"
      />
      <button on:click={checkUrl} class="btn btn-outline btn-accent"
        >Check</button
      >
    </div>
    <p class="text-sm bg-gray-200 bg-opacity-30 px-1 rounded-lg">
      please enter the url in http(s)://www.example.com format
    </p>
    <p class="text-center text-info hover:scale-105"><a href="/process">check how this whole process works!</a></p>
  </div>

  {#if checked}
    <div
      class="flex flex-col space-y-1 mx-4 transition:fade={{
        delay: 300,
        duration: 400,
      }}"
    >
      <p class="text-xl" transition:fade={{
        delay: 200,
        duration: 400,
      }}>
        <span>Trustability Score:</span><span class={scoreColor}>{score}</span
        >/100
      </p>
      <p class="text-center" transition:fade={{
        delay: 300,
        duration: 400,
      }}>
        {#if score > 85}
          <span class="text-green-600">The website is safe to visit!</span>
        {:else if score > 70}
          <span class="text-yellow-500">This website is safe to visit!</span>
        {:else if score > 50}
          <span class="text-amber-700"
            >This website is doesn't seem safe, please be careful.</span
          >
        {:else}
          <span class="text-error"
            >This website is definately not safe to visit, Avoid this website!</span
          >
        {/if}
      </p>
    </div>
  {/if}
  <Info />
</div>
