<script>
    import "../app.css";
  </script>
  
  <slot />
  <style lang="postcss">
    :global(html) {
      background-color: theme(colors.slate.300);
      margin: 2rem;
    }
  </style>