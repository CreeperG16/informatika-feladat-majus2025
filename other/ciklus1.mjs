console.log("- 1. feladat");
for (let i = 10; i --> 0; ) if ((10 - i) % 2 === 0) console.log(10 - i);

console.log(
    new Array(10)
        .fill(1)
        .map((_, i) => i + 1)
        .filter((x) => !(x % 2))
        .join(", ")
);

console.log("\n- 2. feladat");
for (let i = 11; i --> 1; ) console.log(i);

console.log(
    new Array(10)
        .fill(1)
        .map((_, i) => 10 - i)
        .join(", ")
);

console.log("\n- 3. feladat");
for (let i = 10; i --> 0; ) if (i % 2) console.log(i);

console.log(
    new Array(10)
        .fill(1)
        .map((_, i) => 10 - i)
        .filter((x) => x % 2)
        .join(", ")
);

const readline = (out) =>
    new Promise((resolve) => {
        let input = "";
        const listener = (data) => {
            input += data.toString();
            if (!input.endsWith("\n")) return;
            process.stdin.off("data", listener);
            resolve(input.slice(0, -1));
        };
        process.stdin.on("data", listener);
        process.stdout.write(out);
    });

console.log("\n- 4. feladat");

const text = await readline("Mi legyen a szöveg? ");
const n = await readline("Hányszor írja ki a szöveget? ").then(Number);
for (let i = n; i --> 0; ) console.log(text);

console.log("\n- 5. feladat");
while (await readline("Egy páros szám: ").then(Number) % 2);

console.log("\n- 6. feladat");
const nums = new Array(20).fill(1).map(() => Math.ceil(Math.random() * 12));
const three = nums.filter(x => !(x % 3));
console.log(three.join(", "));
console.log(`Összesen ${three.length} darab hárommal osztható szám lett generálva.`);

process.exit(0);
