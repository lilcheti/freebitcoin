
  var config = {
    bet: { label: 'bet', value: 10, type: 'number' },
    payout: { label: 'payout', value: 2, type: 'number' },
    netwin: { label: 'netwin', value: 10, type: 'number' },
    level: { label: 'level', value: 0, type: 'number' },
    loss: { label: 'loss', value: 0, type: 'number' },
    k: { label: 'k', value: 5, type: 'number' },
  }
  
  function main () {
    game.onBet = function () {
      game.bet(config.bet.value, config.payout.value).then(function(payout) {
        if (payout > 1) {
          log.success("We won, netwin " + config.netwin.value + "sats!");
          config.level.value = 0;
          config.netwin.value=10;
          config.bet.value=10;
          config.loss.value=0;
        } else {
          config.level.value +=1;
          config.loss.value += config.bet.value;
          config.netwin.value += config.k.value;
          config.bet.value = config.loss.value+config.netwin.value;
          log.error("lvl"+config.level.value+" We lost, next bet: " + config.bet.value + ", loss: "+config.loss.value+", netwin: "+config.netwin.value);
        }
      });
    }
  }
  