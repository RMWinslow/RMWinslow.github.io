document.write(`
<div class="rulesBlock"   style="background-color: hsl(22, 100%, 64%);">
    <center>
        <img src="imgs/fox2.svg" class="lch">
        <img src="imgs/fox2.svg" class="rch">
        <h4 id="foxInTheForest"> Fox in the Forest</h4> 
        <p><i>By Joshua Buergel. YET TO PLAY </i></p>
        <p>(2) <a href="tricktaking.html">Trick-Taking</a>. 3 Suits, A-10 and Q.</p>
    </center>
    <div class="rulesBody"  style="background-color: hsl(30, 100%, 90%)">
        <ul>
        <li>Cards are ranked QX98765432A, high to low. (Ace low).</li>
        <li>Each hand, deal 13 cards to each player. Flip a card to determine Trump.</li>
        <li>Some cards have special effects when played in a trick:</li>
            <ul>
            <li><span class="card">A</span>: You lead the next Trick if you lose this one.</li>
            <li><span class="card">3</span>: Immediately swap the trump card with a card from your hand.</li>
            <li><span class="card">5</span>: Immediately draw one card and then place a card from your hand on the bottom of the deck.</li>
            <li><span class="card">7</span>: +1 point to whoever takes this trick.</li>
            <li><span class="card">9</span>: If only one 9 was played at the end of a trick, treat it like a trump suit.</li>
            <li><span class="card">Q</span>: If your opponent can follow suit, they must either play an A or their highest card in this suit.</li>
            </ul>
        <li>End of Hand Scoring:</li>
            <ul>
            <li>0-3 Tricks: +6 Points</li>
            <li>4 Tricks: +1 Points</li>
            <li>5 Tricks: +2 Points</li>
            <li>6 Tricks: +3 Points</li>
            <li>7-9 Tricks: +6 Points</li>
            <li>10-13 Tricks: +0 Points</li>
            </ul>
        <li>First player to 16/21/35 points wins.</li>
        </ul>
    </div>
</div><br>
`)