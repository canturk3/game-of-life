const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');

const GRID_SIZE = 30;
const CELL_SIZE = 20; // each cell's width/height in pixels
const MARGIN = 5; // margin between cells
const WIDTH = CELL_SIZE;
const HEIGHT = CELL_SIZE;
const BLACK = '#000000';
const GREEN = '#00FF00';

let grid = [];
let simulationInterval = null;

function initGrid() {
    grid = [];
    for (let row = 0; row < GRID_SIZE; row++) {
        const line = [];
        for (let col = 0; col < GRID_SIZE; col++) {
            line.push(0);
        }
        grid.push(line);
    }
}

function drawCell(row, col, state) {
    const x = (MARGIN + WIDTH) * col + MARGIN;
    const y = (MARGIN + HEIGHT) * row + MARGIN;
    ctx.fillStyle = state === 1 ? GREEN : BLACK;
    ctx.fillRect(x, y, WIDTH, HEIGHT);
}

function drawGrid() {
    ctx.fillStyle = BLACK;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    for (let row = 0; row < GRID_SIZE; row++) {
        for (let col = 0; col < GRID_SIZE; col++) {
            drawCell(row, col, grid[row][col]);
        }
    }
}

function getNeighbourCount(row, col) {
    let count = 0;
    for (let nRow = row - 1; nRow <= row + 1; nRow++) {
        for (let nCol = col - 1; nCol <= col + 1; nCol++) {
            if (nRow === row && nCol === col) continue;
            if (nRow >= 0 && nRow < GRID_SIZE && nCol >= 0 && nCol < GRID_SIZE) {
                if (grid[nRow][nCol] === 1) count++;
            }
        }
    }
    return count;
}

function simulationStep() {
    const neighbourGrid = [];
    for (let row = 0; row < GRID_SIZE; row++) {
        neighbourGrid[row] = [];
        for (let col = 0; col < GRID_SIZE; col++) {
            neighbourGrid[row][col] = getNeighbourCount(row, col);
        }
    }

    for (let row = 0; row < GRID_SIZE; row++) {
        for (let col = 0; col < GRID_SIZE; col++) {
            const neighbours = neighbourGrid[row][col];
            if (grid[row][col] === 1) {
                if (neighbours !== 2 && neighbours !== 3) grid[row][col] = 0;
            } else {
                if (neighbours === 3) grid[row][col] = 1;
            }
        }
    }
    drawGrid();
}

function toggleSimulation() {
    if (simulationInterval) {
        clearInterval(simulationInterval);
        simulationInterval = null;
    } else {
        simulationInterval = setInterval(simulationStep, 100);
    }
}

canvas.addEventListener('mousedown', (e) => {
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const col = Math.floor(x / (WIDTH + MARGIN));
    const row = Math.floor(y / (HEIGHT + MARGIN));
    if (row >= 0 && row < GRID_SIZE && col >= 0 && col < GRID_SIZE) {
        grid[row][col] = 1;
        drawCell(row, col, 1);
    }
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'x' || e.key === 'X') {
        toggleSimulation();
    }
});

initGrid();
drawGrid();
