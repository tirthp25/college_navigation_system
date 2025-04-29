const canvas = document.getElementById("path-canvas");
const ctx = canvas.getContext("2d");

if (path && path.length > 1) {
    ctx.strokeStyle = "red";
    ctx.lineWidth = 3;
    ctx.beginPath();

    const start = positions[path[0]];
    ctx.moveTo(start[0], start[1]);

    for (let i = 1; i < path.length; i++) {
        const pos = positions[path[i]];
        ctx.lineTo(pos[0], pos[1]);
    }

    ctx.stroke();
}
