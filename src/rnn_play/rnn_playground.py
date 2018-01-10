from sys import argv

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

if __name__ == "__main__":
    main()
