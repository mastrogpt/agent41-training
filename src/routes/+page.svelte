<script lang="ts">
    import { onMount } from "svelte";

    onMount(() => {
        const target = document.getElementById("target") as HTMLIFrameElement;
        if (!target?.contentWindow) return;
        fetch("/api/my/mastrogpt/index")
            .then((response) => response.json())
            .then((data) => {
                //console.log(data);
                const msg = {
                    type: "metadata",
                    data: { namespace: data.username },
                };
                target.contentWindow!.postMessage(msg, target.src);
            });
    });
    
</script>

<button>Click me</button>

<iframe
    id="target"
    src="https://pinocchio.nuvolaris.org"
    title="MastroGPT Interface"
></iframe>

<style>
    button {
        margin: 0.5rem;
        padding: 0.5rem 0.5rem;
    }
    
    iframe {
        position: absolute;
        inset: 0;
        top: 4rem; /* Leave space for button */
        border: none;
        width: 100%;
        height: calc(100% - 4rem);
    }
</style>
