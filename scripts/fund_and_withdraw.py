from brownie import FundMe
from time import sleep
from scripts.helpful_Scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"current entrance fee is {entrance_fee}")
    sleep(2)
    print("funding...")
    sleep(3)
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing funds...")
    sleep(3)
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
