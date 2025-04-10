<script lang="ts">
	let { children } = $props();

	import "../app.css";
	import Head from "$lib/components/Head.svelte";
	import Sidebar from "$lib/components/Sidebar.svelte";
	import Header from "$lib/components/Header.svelte";

</script>

<!DOCTYPE html>
<html lang="en" class="h-full bg-white">
	<head>
		<Head />
	</head>

	<body class="h-full">
		<div>
			<Sidebar />
			<div class="lg:pl-72">
				<Header />
				<main class="py-10">
					<div class="px-4 sm:px-6 lg:px-8">
						{@render children() }
					</div>
				</main>
			</div>
		</div>
	</body>
</html>
