def tests():

    small_container_number = input("How many small (less than 1L) containers do you have?")
    large_container_number = input("How many large (more than 1L) containers do you have?")
    
    refund_small = small_container_number * 0.10
    refund_large = large_container_number * 0.25
    
    total_refund = refund_small + refund_large
    print ("Total refund is ${}".format(total_refund))

tests()
  