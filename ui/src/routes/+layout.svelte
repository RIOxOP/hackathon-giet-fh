<script>
    import "../app.css";
  import Footer from "../lib/footer.svelte";
  import Navbar from "../lib/navbar.svelte";
  </script>
  
  <div class="flex flex-col h-screen justify-between">
    <Navbar />
    <slot />
    <Footer />
  </div>


  <style lang="postcss">
    :global(html) {
      background-color: theme(colors.slate.300);
      margin-top: 0.5rem;
      margin-right: 2rem;
      margin-left: 2rem;
    }
  </style>