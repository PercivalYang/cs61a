(define (add-to-end lst x)
  (if (null? (car lst))
      x)
  (list (car lst) (add-to-end (cdr lst x))))
