from brownie import FundMe
from .utils import get_account


def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy({"from": account}, publish_source=True)
    print(f"contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
