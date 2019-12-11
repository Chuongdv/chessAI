import source.table
import chess
import math
import source.table

import chess.polyglot

isExistInOpeningBook = True;

def makeBestMove(depth, game, isMaximisingPlayer):
    exMove = experienceMove(game);
    if exMove is None:
        return minimaxRoot(depth, game, isMaximisingPlayer);
    else:
        return exMove;


def experienceMove(game):
    with chess.polyglot.open_reader("../data/opening/proDeo.bin") as reader:
        opening_moves = [
            str(entry.move) for entry in reader.find_all(game)
        ];
        if opening_moves:
            for move in opening_moves:

                return move
        else:
            return None


def minimaxRoot(depth, game, isMaximisingPlayer):
    legal_moves = [str(legal_move) for legal_move in game.legal_moves];
    bestMove = -math.inf;
    bestMoveFound = "abc";

    for newMove in legal_moves:
        game.push(chess.Move.from_uci(newMove));
        value = minimax(depth - 1, game, -math.inf, math.inf, not (isMaximisingPlayer));
        game.pop();
        if (value >= bestMove):
            bestMove = value;
            bestMoveFound = newMove;

    return bestMoveFound;


def minimax(depth, game, alpha, beta, isMaximisingPlayer):
    if (depth == 0):
        return -evaluateBoard(game);

    legal_moves = [str(legal_move) for legal_move in game.legal_moves];

    if (isMaximisingPlayer):
        bestMove = -math.inf;
        for newMove in legal_moves:
            game.push(chess.Move.from_uci(newMove));
            bestMove = max(bestMove, minimax(depth - 1, game, alpha, beta, not isMaximisingPlayer));
            game.pop();
            alpha = max(alpha, bestMove);
            if beta <= alpha:
                return bestMove;

        return bestMove;

    else:

        bestMove = math.inf;
        for newMove in legal_moves:
            game.push(chess.Move.from_uci(newMove));
            bestMove = min(bestMove, minimax(depth - 1, game, alpha, beta, not isMaximisingPlayer));
            game.pop();
            beta = min(beta, bestMove);
            if beta <= alpha:
                return bestMove;

        return bestMove;


def evaluateBoard(game):
    totalEvaluation = 0;
    for square in chess.SQUARES:
        totalEvaluation += getPieceValue(game, square);
    return totalEvaluation;


def getPieceValue(game, square):
    piece = game.piece_at(square);
    if piece is None:
        return 0;

    def getAbsoluteValue(piece, isWhite, square):
        row = convert_square(square)[0]
        col = convert_square(square)[1]
        if piece.symbol().lower() == 'p':
            return 100 + (source.table.pawnEvalWhite[row][col] if isWhite else source.table.pawnEvalBlack[row][col]);
        elif piece.symbol().lower() == 'n':
            return 320 + source.table.knightEval[row][col];
        elif piece.symbol().lower() == 'b':
            return 330 + (source.table.bishopEvalWhite[row][col] if isWhite else source.table.bishopEvalBlack[row][col]);
        elif piece.symbol().lower() == 'r':
            return 500 + (source.table.rookEvalWhite[row][col] if isWhite else source.table.rookEvalBlack[row][col]);
        elif piece.symbol().lower() == 'q':
            return 900 + source.table.evalQueen[row][col];
        elif piece.symbol().lower() == 'k':
            return 20000 + (source.table.kingEvalWhite[row][col] if isWhite else source.table.kingEvalBlack[row][col]);

    absoluteValue = getAbsoluteValue(piece, game.color_at(square), square);

    return absoluteValue if game.color_at(square) else -absoluteValue;


def convert_square(square):
    row = (square // 8);
    column = square % 8;
    return (row, column)



