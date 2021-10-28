from solana.rpc.api import Client
from solana.publickey import PublicKey
import time
solana_client = Client("https://api.mainnet-beta.solana.com")

import requests






def solanart_nft_user(user_address):
    x=1
    current_time=time.time()
    #solanartのtxを抽出
    sol_detail=solana_client.get_signatures_for_address(user_address, limit=100)
    while True:
        try:
            #tx抽出
            sol_tx=sol_detail["result"][x]["signature"]
                        
            #tx詳細を抽出
            solana_owner=solana_client.get_confirmed_transaction(sol_tx)
            #NFTの詳細
            token_address=solana_owner["result"]["meta"]["preTokenBalances"][0]["mint"]
            #print(token_address)
            #NFTのtx
            token_tx=solana_client.get_signatures_for_address(token_address)
            #nftの最初のtxを抽出
            block_time=token_tx["result"][-1]["blockTime"]
            owner_balance=solana_owner["result"]["meta"]["postBalances"][0]/10**9
            owner_prebalance=solana_owner["result"]["meta"]["preBalances"][0]/10**9
            price = owner_prebalance-owner_balance
            owner_balance=solana_owner["result"]["meta"]["postBalances"][0]/10**9

            
            if 0.1< price <1.5:
                owner_address=solana_owner["result"]["transaction"]["message"]["accountKeys"][0]
                token_address=solana_owner["result"]["meta"]["preTokenBalances"][0]["mint"]
                owner_prebalance=solana_owner["result"]["meta"]["preBalances"][0]/10**9
                price = owner_prebalance-owner_balance

                print("オーナーアドレス："+str(owner_address))
                print("オーナー残高："+str(owner_balance))
                print("NFT価格:"+str(price))
                print("NTFアドレス： https://explorer.solana.com/address/"+str(token_address))
                

                x+=1
                time.sleep(1)
                
                
            else:
                x+=1
                time.sleep(1)
                    
                    
            
                    
                    
            
        except IndexError as e:
            print(e)
            print(x)
            break




if __name__=="__main__":
    solanart_nft_user(user_address)
    
    


    