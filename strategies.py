"""
Some example strategies for people who want to create a custom, homemade bot.

With these classes, bot makers will not have to implement the UCI or XBoard interfaces themselves.
"""

from __future__ import annotations
import chess
from chess.engine import PlayResult
import random
from engine_wrapper import MinimalEngine
from typing import Any, Union
import logging

from engines.termoman import find_best_move
MOVE = Union[chess.engine.PlayResult, list[chess.Move]]


# Use this logger variable to print messages to the console or log files.
# logger.info("message") will always print "message" to the console or log file.
# logger.debug("message") will only print "message" if verbose logging is enabled.
logger = logging.getLogger(__name__)

class TermomanEngine(MinimalEngine):
    def search(self, board: chess.Board, *args: Any) -> PlayResult:
        """Aplha Beta pruning implementation."""
        depth = 3

        return PlayResult(find_best_move(board, depth), None)