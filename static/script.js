document.getElementById("btn").addEventListener("click", async function() {
	document.getElementById("btn").disabled = true;
	document.getElementById("video-location").innerHTML = "<progress></progress>"
	document.getElementById("btn").innerHTML = "Fetching your motivation ...";

	let response = await fetch('http://localhost:5000/getvid/');
	if (response.ok) {
		console.log(response);
		// const filename = response.headers.get('content-disposition').split('filename=')[1];
		const blob = await response.blob();
		const url = window.URL.createObjectURL(blob);
		console.log(url);
		document.getElementById("video-location").innerHTML =
			`
			<div style="justify-content: center">
				<video>  </video>
			</div>
		`
		let video = document.getElementsByTagName("video")[0];
		video.setAttribute("src", url);
		video.load(); video.play();
	} else {
		console.log("OOOUUUPS");
	}

	document.getElementById("btn").disabled = false;
	document.getElementById("btn").innerHTML = "Get motivational video";
})

