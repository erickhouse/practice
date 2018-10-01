
class Node {
    constructor(value, children){
        this.value = value;
        this.children = children;
    }
}

let four = new Node(4, []);
let three = new Node(3, [four]);
let two = new Node(2, [three, four]);
let root = new Node(1, [two, four]);

let doWork = (node) => console.log(node.value);

function bfs(root) {

    let visited = new Set();

    let q = [root];
    while(q.length != 0) {
        let head = q.shift();
        if(!visited.has(head)){
            doWork(head);
            q = q.concat(head.children);
            visited.add(head);
        }
    }
}

function dfs(root) {
    let visited = new Set();
    function recDfs(node) {

        if(visited.has(node)){
            return;
        }
        visited.add(node);
        doWork(node);
        node.children.forEach(child => {
            recDfs(child);
        });

    }
    recDfs(root);
}
