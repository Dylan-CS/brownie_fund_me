from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account, 
    deploy_mocks, 
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
)

def deploy_fund_me():
    account =get_account()
    # pass the price feed address to our fundme address\
    # if we are on a pesistent network like goerli,use the associated address
    # otherwise , deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address= config["networks"][network.show_active()]["eth_used_price_feed"]
    else:
        deploy_mocks()
        price_feed_address= MockV3Aggregator[-1].address


    fund_me = FundMe.deploy(
        price_feed_address,
        {"from":account},
        publish_source=config["networks"][network.show_active()].get("vertify"),
        )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()