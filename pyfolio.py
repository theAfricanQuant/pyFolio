# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2018-08-27 19:28:58
# @Last Modified by:   boyac
# @Last Modified time: 2018-08-27 20:26:33


def allocation_effect():
	return (portw-benchw)*(benchr-benchtotal)


def selection_effect():
	return portw*(portr-benchr)


def interaction_effect():
	return (portw-benchw)*(portr-benchr)


def active_effect():
	active = allocation_effect()+selection_effect()+interaction_effect() 
	return "{:.2%}".format(active)


def PME():
	#ticker, trade_dt, quantity, unit_cost, cost_basis, start_yr, dt, adj_cost, ticker_return
	#index_close, index_st_close, share_ytd, index_ytd, cum_invst, cum_tic_return
	pass



if __name__ == "__main__":
	#Benchmark S&P500
	#Bechmark segment S&P500 Tech
	#Benchmark return 9%
	#Benchmark weight 7%
	#Benchmark tech return 8%
	#Benchmark tech weight 15%
	#Total benchmark return 7%

	benchr=0.09
	benchw=0.07
	portr=0.08
	portw=0.15
	benchtotal=0.07

	print allocation_effect()
	print selection_effect()
	print interaction_effect()
	print active_effect()
