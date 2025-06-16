#!/usr/bin/env python3

"""
测试新的ticker选择功能
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cli.main import get_ticker
from rich.console import Console

console = Console()

def test_ticker_selection():
    """测试ticker选择功能"""
    console.print("[bold green]🚀 测试TradingAgents股票选择功能[/bold green]\n")
    
    try:
        selected_ticker = get_ticker()
        console.print(f"\n[bold green]✅ 成功选择股票: {selected_ticker}[/bold green]")
        
        # 显示一些关于所选股票的信息
        popular_stocks = {
            "SPY": "SPDR S&P 500 ETF Trust - 跟踪标普500指数的ETF",
            "AAPL": "Apple Inc. - 美国科技巨头，iPhone制造商",
            "MSFT": "Microsoft Corporation - 美国软件巨头",
            "NVDA": "NVIDIA Corporation - GPU和AI芯片领导者",
            "GOOGL": "Alphabet Inc. - Google母公司",
            "TSLA": "Tesla Inc. - 电动汽车和清洁能源公司",
            "AMZN": "Amazon.com Inc. - 电商和云计算巨头",
            "META": "Meta Platforms Inc. - Facebook母公司",
        }
        
        if selected_ticker in popular_stocks:
            console.print(f"[cyan]📊 {popular_stocks[selected_ticker]}[/cyan]")
        else:
            console.print(f"[cyan]📊 您选择了自定义股票: {selected_ticker}[/cyan]")
            
        console.print(f"\n[yellow]💡 提示: 该股票将用于TradingAgents多智能体分析系统[/yellow]")
        
    except KeyboardInterrupt:
        console.print("\n[red]❌ 测试被用户中断[/red]")
    except Exception as e:
        console.print(f"\n[red]❌ 测试出错: {e}[/red]")

if __name__ == "__main__":
    test_ticker_selection() 