


document.write(`
<div class="rulesBlock"   style="">
    <center>
        <img src="imgs/die.svg" class="lch">
        <img src="imgs/slot.svg" class="lch">
        <img src="imgs/die.svg" class="rch">
        <img src="imgs/slot.svg" class="rch">
        <h4 id="reno">Reno</h4> 
        <p><i>By Rüdiger Dorn<br>YET TO PLAY</i></p>
        <p>(3-5). Standard Deck, no Jokers; dice.</p>
    </center>
    <div class="rulesBody"  style="">
        <ul>
        <li>Each player gets 8 dice of their color and 2 neutral dice.</li>
        <li>Deal Out 6 stacks of cards on the table:<li>
            <ul>
            <li>Deal cards to a stack until the cards add up to at least 7 in total.</li>
            <li>Arrange each stack from highest to lowest.</li>
            </ul>
        <li>Each turn:</li>
            <ul>
            <li>Roll all dice in your pool.</li>
            <li>Choose a number from 1 to 6. </li>
            <li><i>All</i> your dice which rolled that number are played to the cooresponding stack.</li>
            </ul>
        <li>Once all dice are played out:</li>
            <ul>
            <li>For each stack, the player with the most dice takes the highest card.</li>
            <li>The player with the second-most takes the second highest, etc.</li>
            <li>Ties cancel each other out.</li>
            <li>The nuetral color can win cards and tie with players.</li>
            </ul>
        <li>After four rounds, score:</li>
            <ul>
            <li><span class="card">J</span>, <span class="card">Q</span>, and <span class="card">K</span> are worth 11, 12, and 13, respectively.</li>
            <li><span class="card">A</span> are worth 1 point but are placed at the top of stacks.</li>
            <li>All other cards are worth their face value.</li>
            </ul>
        </ul>
    </div>
</div><br>
`)