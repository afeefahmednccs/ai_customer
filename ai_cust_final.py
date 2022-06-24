from ai_cust_code import final_outcome

def final_function():
    filename='Intro.wav'
    response=final_outcome(filename)
    if(response=='POSITIVE'):
        filename = 'Programe Info.wav'
        response = final_outcome(filename)
        if (response == 'POSITIVE'):
            filename = 'Qualification Question.wav'
            response = final_outcome(filename)
            if (response == 'POSITIVE'):
                filename = 'Are your Still Making payments on time.wav'
                response = final_outcome(filename)
                if (response == 'POSITIVE'):
                    filename = 'Hold On Let me Trasnfer.wav'
                    response = final_outcome(filename)
                    if (response == 'POSITIVE'):
                        filename = 'Trasnfeing-Confernce.wav'
                        response = final_outcome(filename)
                        if (response == 'POSITIVE'):
                            filename = 'Trasnfer to Agent.wav'
                            response = final_outcome(filename)
                        else:
                            print('Sorry, we Dropped your call Thanks.')
                    else:
                        print('Sorry, we Dropped your call Thanks.')
                else:
                    print('Sorry, we Dropped your call Thanks.')
            else:
                print('Sorry, we Dropped your call Thanks.')
        else:
            print('Sorry, we Dropped your call Thanks.')
    else:
        print('Sorry, we Dropped your call Thanks.')

        
        
       







