import os
import sys
import random
from web3 import Web3
import json
import ast
from datetime import date

from mnemonic import Mnemonic
mnemo = Mnemonic("english")
infura_url = {
	"BSC":"https://cold-nameless-paper.bsc.discover.quiknode.pro/8d4b7d41d4545495178323787ad17b44bc41e0e2/",
	"ETH":"https://serene-withered-tab.discover.quiknode.pro/f485a39be346d4436604f689989e073c9fc7e4c8/",
	"POLYGON":"https://neat-nameless-market.matic.discover.quiknode.pro/f2ccfd55605089ff8df1ad6b7f805f43d52d369c/",
	"ARBITRUM":"https://quiet-divine-morning.arbitrum-mainnet.discover.quiknode.pro/9d2fd910fd8be290210486d65911db2b1159245c/",
	"AVALANCHE":"https://responsive-divine-friday.avalanche-mainnet.discover.quiknode.pro/c6104b47cfe9decf8cac1eed5b2d901f2d5ae23f/ext/bc/C/rpc/",
	"OPTIMISM":"https://alien-black-forest.optimism.discover.quiknode.pro/84c7fb95fcc6f2ff5ef5bc2c5d70b6ea14195103/"
}
Tokens={
	"BSC": {
		"ETH":"0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
	 	"USDT":"0x55d398326f99059fF775485246999027B3197955",
		"WBNB":"0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
		"USDC":"0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",
		"XRP":"0x1D2F0da169ceB9fC7B3144628dB156f3F6c60dBE",
		"BUSD":"0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
		"MATIC":"0xCC42724C6683B7E57334c4E856f4c9965ED682bD"
		},
	"ETH":{
		"WETH":"0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
		"USDT":"0xdAC17F958D2ee523a2206206994597C13D831ec7",
		"BNB":"0xB8c77482e45F1F44dE1745F52C74426C631bDD52",
		"USDC":"0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
		"stETH":"0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84",
		"TRON":"0x50327c6c5a14DCaDE707ABad2E27eB517df87AB5",
		"MATIC":"0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0",
		"THETA":"0x3883f5e181fccaF8410FA61e12b59BAd963fb645",
		"BUSD":"0x4Fabb145d64652a948d72533023f6E7A623C7C53",
		"DAI":"0x6B175474E89094C44Da98b954EedeAC495271d0F",
		"WBTC":"0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
		"UNI":"0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984",
		"TUSD":"0x0000000000085d4780B73119b644AE5ecd22b376",
		"LINK":"0x514910771AF9Ca656af840dff83E8264EcF986CA"
	},
	"POLYGON":{
		"USDT":"0xc2132D05D31c914a87C6611C10748AEb04B58e8F",
		"BNB":"0x3BA4c387f786bFEE076A58914F5Bd38d668B42c3",
		"USDC":"0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
		"BUSD":"0xdAb529f40E671A1D4bF91361c21bf9f0C9712ab7",
		"DAI":"0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063",
		"AVAX":"0x2C89bbc92BD86F8075d1DEcc58C7F4E0107f286b",
		"WBTC":"0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6",
		"SAND":"0xBbba073C31bF03b8ACf7c28EF0738DeCF3695683"
	},
	"ARBITRUM":{
		"USDT":"0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
		"USDC.e":"0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
		"USDC":"0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
		"DAI":"0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
		"WBTC":"0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f",
		"ARB":"0x912CE59144191C1204E64559FE8253a0e49E6548",
		"GMX":"0xfc5A1A6EB076a2C7aD06eD22C90d7E710E35ad0a"
	},
	"AVALANCHE":{
		"USDT.e":"0xc7198437980c041c805A1EDcbA50c1Ce5db95118",
		"USDT":"0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7",
		"USDC":"0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E",
		"USDC.e":"0xA7D7079b0FEaD91F3e65f86E8915Cb59c1a4C664",
		"BUSD.e":"0xd586E7F844cEa2F87f50152665BCbc2C279D8d70",
		"BUSD":"0x9C9e5fD8bbc25984B178FdCE6117Defa39d2db39",
		"WAVAX":"0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7",
		"WBTC.e":"0x50b7545627a5162F82A992c33b87aDc75187B218"
	},
	"OPTIMISM":{
		"OP":"0x4200000000000000000000000000000000000042",
		"USDT":"0x94b008aA00579c1307B0EF2c499aD98a8ce58e58",
		"USDC":"0x7F5c764cBc14f9669B88837ca1490cCa17c31607",
		"DAI":"0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
		"WBTC":"0x68f180fcCe6836688e9084f035309E29Bf0A2095",
		"LINK":"0x350a791Bfc2C21F9Ed5d10980Dad2e2638ffa7f6"
	},
	"FANTOM":{
		"FBTC":"0xe1146b9AC456fCbB60644c36Fd3F868A9072fc6E",
		"FETH":"0x658b0c7613e890EE50B8C4BC6A3f41ef411208aD",
		"USDC":"0x04068DA6C83AFCFA0e13ba15A6696662335D5B75",
		"DAI":"0x8D11eC38a3EB5E956B052f67Da8Bdc9bef8Abf3E",
		"AVAX":"0x511D35c52a3C244E7b8bd92c0C297755FbD89212",
		"BTC":"0x321162Cd933E2Be498Cd2267a90534A804051b11",
	}

}


# seed = mnemo.to_seed(words, passphrase="")
# print("seed:", seed)
seed_words = []
def gen_seed():
	if len(seed_words) == 0:
		return ""
	seed = ""
	while not mnemo.check(seed):
		seed_list = random.choices(seed_words, k=12)
		seed = " ".join(seed_list)
		# web3.eth.account.hdaccount.mnenonic
		# mnemo.check(seed)
	# print("seed: ", seed)
	return seed


def get_words():
	f =  open ("english.txt", 'r' ) 
	words = f.read().split("\n")
	f.close()
	return words

def get_addr():
	words = mnemo.generate(strength=128)
	# print("words:", words)
	return words

def address_export():
	pkey_path = "address_file"
	pkey_f = open(pkey_path, "a", encoding = "utf-8")

	mnemonic_file = "mnemonic_file"
	web3 = Web3(Web3.HTTPProvider(infura_url["BSC"]))
	web3.eth.account.enable_unaudited_hdwallet_features()
	mnemonic_f = open(mnemonic_file, "r", encoding="utf-8")
	data =  mnemonic_f.readlines()
	mnemonic_f.close()
	n=0
	for line in data:
		n=n+1
		line=line.strip()
		if not line:continue
		# line=json.loads(line)


		line = ast.literal_eval(line)
		print(line)


		my_mnemonic = line["result"][0]["data"]["mnemonic"]
		n_accounts = line["result"][0]["data"]["numberOfAccounts"]
		
		for i in range(n_accounts+1):
			account = web3.eth.account.from_mnemonic(my_mnemonic, account_path="m/44'/60'/0'/0/"+str(i))
			wallet_addr = account.address
			wallet_pkey = account.key.hex()
			pkey_f.write(wallet_addr+" : "+str(wallet_pkey)[2:]+"\n")
		for item in line["result"]:
			if item["type"] == "Simple Key Pair":
				wallet_pkey = item["data"][0]
				wallet_addr =  web3.eth.account.privateKeyToAccount(wallet_pkey).address
				pkey_f.write(wallet_addr+" : "+wallet_pkey+"\n")
	pkey_f.close()
def address_only_export():
	addr_list =[]
	pkey_path = "address_only_file"
	pkey_f = open(pkey_path, "r", encoding = "utf-8")
	addrs = pkey_f.readlines()
	pkey_f.close()
	for addr in addrs:
		addr = addr.strip()
		if not addr in addr_list:
			addr_list.append(addr)

	pkey_f = open(pkey_path, "a", encoding = "utf-8")

	mnemonic_file = "mnemonic_file"
	web3 = Web3(Web3.HTTPProvider(infura_url["BSC"]))
	web3.eth.account.enable_unaudited_hdwallet_features()
	mnemonic_f = open(mnemonic_file, "r", encoding="utf-8")
	data =  mnemonic_f.readlines()
	mnemonic_f.close()
	n=0
	for line in data:
		n=n+1
		line=line.strip()
		if not line:continue
		# line=json.loads(line)


		line = ast.literal_eval(line)
		print(line)


		my_mnemonic = line["result"][0]["data"]["mnemonic"]
		n_accounts = line["result"][0]["data"]["numberOfAccounts"]
		
		for i in range(n_accounts):
			account = web3.eth.account.from_mnemonic(my_mnemonic, account_path="m/44'/60'/0'/0/"+str(i))
			wallet_addr = account.address
			wallet_pkey = account.key.hex()
			if not wallet_addr in addr_list:
				addr_list.append(wallet_addr)
				pkey_f.write(wallet_addr+"\n")
		for item in line["result"]:
			if item["type"] == "Simple Key Pair":
				wallet_pkey = item["data"][0]
				wallet_addr =  web3.eth.account.privateKeyToAccount(wallet_pkey).address
				if not wallet_addr in addr_list:
					addr_list.append(wallet_addr)
					pkey_f.write(wallet_addr+"\n")
	pkey_f.close()

def check_balance():
	abi = json.load(open("ERC20.json"))

	
	address_list =[]
	address_file="address_only_file"
	add_f = open(address_file,"r",encoding="utf-8")
	address_list = add_f.read().split("\n")
	add_f.close()
	w_number =0
	start =False
	for addr in address_list:
		w_number +=1
		if addr.strip() == "": continue
		wallet = addr.strip().split(" : ")[0]
		if start==False and wallet!="0x1bE74edCAe150d3b57660d1C46FE423DD7C0eB6D":
			continue
		start =True
		print("wallet: ", wallet)
		res_f = open("result","a",encoding="utf-8")
		if w_number ==1:res_f.write("\n\n_________________________________"+str(date.today())+"__________________________________\n")
		for chain in infura_url.keys():
			web3 = Web3(Web3.HTTPProvider(infura_url[chain]))
			web3.eth.account.enable_unaudited_hdwallet_features()
			balance_native = web3.eth.getBalance(wallet)
			if balance_native >= 1E10:
				balance_native = web3.fromWei(balance_native,"ether")
				print(chain, "native " + str(balance_native))
				res_f.write(wallet + " "+ chain + " native " + str(balance_native)+"\n")
			# print(Tokens[chain])
			for key,val in Tokens[chain].items():
				contract = web3.eth.contract(address = val, abi = abi)
				balance_token = contract.functions.balanceOf(wallet).call()
				decimals = contract.functions.decimals().call()
				
				
				dif = 1
				if "usdt" in key.lower() or "usdc" in key.lower():dif = 0
				if "btc" in key.lower() or "eth" in key.lower():dif = 3
				threshold = 0#10**(decimals-dif)
				if balance_token > threshold:
					balance_t = web3.fromWei(balance_token,"ether")
					if decimals ==6:balance_t = web3.fromWei(balance_token,"mwei")
					print(chain, key, str(balance_t))
					res_f.write(wallet + " "+ chain + " " + key + " "+str(balance_t)+"\n")
		res_f.close()

# address_only_export()
check_balance()