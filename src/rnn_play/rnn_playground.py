from abc import ABC, abstractmethod
from typing import Callable, Tuple, Sequence

import numpy as np
from sklearn.utils.extmath import softmax


def main():
    print("""TODO
    
    (1) number sequence prediction
        (1.1) (a) function to generate values 
              (b) generate sequence
              (c) train to memorize
        (1.2) (a) generate _many_ sequences
              (b) train over _all_
              (c) predict (*should be worse....)
        (1.3) do (1.2) but with _same family of eqns_ .e.g all linear, polynomial, etc.

    (2) simple question-to-answer LSTM embedding similarity learning
        (a) create a really simple Q/A dataset of 10 things, using _simple_ vocab
        (b) bi-LSTM to encode question, same to encode answer
        (c) training: encode Q,A and make sure they have similiar represnetations
        (d) prediction: for a given Q and set of known answers, retrieve the correct one
    
    """)


class NnUnit(ABC):
    pass
    # @abstractmethod
    # def compute(self, *args, **kwargs) -> Any:
    #     raise NotImplementedError


class RnnUnit(NnUnit, ABC):
    @property
    @abstractmethod
    def h_initial(self) -> np.ndarray:
        raise NotImplementedError

    def sequence(self, x: Sequence[np.ndarray]) -> Tuple[Sequence[np.ndarray], Sequence[np.ndarray]]:
        if len(x) == 0:
            raise ValueError("Input sequence must not be empty.")

        outputs, hidden_states = [], []
        y, h = self.compute(x[0], self.h_initial)
        outputs.append(y)
        hidden_states.append(h)
        for next_x in x[1:]:
            y, h = self.compute(next_x, h)
            outputs.append(y)
            hidden_states.append(h)
        return outputs, hidden_states

    @abstractmethod
    def compute(self, x_t: np.ndarray, h_tm1: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        raise NotImplementedError


class VanillaRnnUnit(RnnUnit):
    def __init__(self, w_h: np.ndarray, b_h: float,
                 w_o: np.ndarray, b_o: float,
                 w_x: np.ndarray,
                 f: Callable[[np.ndarray], np.ndarray],
                 h_initial: np.ndarray) -> None:
        self.w_h = w_h
        self.b_h = b_h
        self.w_o = w_o
        self.b_o = b_o
        self.w_x = w_x
        self.f = f
        self.h_0 = h_initial

    def h_initial(self) -> np.ndarray:
        return self.h_0

    def compute(self, x_t: np.ndarray, h_tm1: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        # calculate new hidden state
        w_t_previous_h = self.w_h.transpose().dot(h_tm1)
        w_t_input = self.w_x.transpose().dot(x_t)
        h_t = self.f(w_t_previous_h + w_t_input + self.b_h)
        # calculate output
        w_t_hidden = self.w_o.transpose().dot(h_t)
        y_t = softmax(w_t_hidden + self.b_o)
        # return output & hidden state
        return y_t, h_t


if __name__ == "__main__":
    main()
