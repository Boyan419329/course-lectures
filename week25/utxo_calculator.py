from typing import List, Tuple, Dict

def select_utxos(utxos: Dict[str, float], send_amount: float, fee: float) -> Tuple[List[str], float]:
    """
    选择合适的UTXO组合并计算找零金额
    
    Args:
        utxos: 字典，键为UTXO ID，值为BTC金额
        send_amount: 要发送的BTC金额
        fee: 交易费用
        
    Returns:
        Tuple[List[str], float]: 返回所选UTXO列表和找零金额
    """
    total_needed = send_amount + fee
    selected_utxos = []
    total_selected = 0.0
    
    # 按金额从大到小排序UTXO
    sorted_utxos = sorted(utxos.items(), key=lambda x: x[1], reverse=True)
    
    # 选择最少数量的UTXO
    for utxo_id, amount in sorted_utxos:
        if total_selected >= total_needed:
            break
        selected_utxos.append(utxo_id)
        total_selected += amount
    
    # 检查是否有足够的金额
    if total_selected < total_needed:
        raise ValueError("UTXO金额不足以支付交易")
    
    # 计算找零金额
    change = total_selected - total_needed
    
    return selected_utxos, change

# 测试代码
if __name__ == "__main__":
    # 小明的UTXO
    utxos = {
        "UTXO1": 0.3,
        "UTXO2": 0.5,
        "UTXO3": 0.2
    }
    
    send_amount = 0.8  # 发送给小红的金额
    fee = 0.1         # 交易费用
    
    try:
        selected, change = select_utxos(utxos, send_amount, fee)
        print(f"选择的UTXO: {selected}")
        print(f"找零金额: {change} BTC")
    except ValueError as e:
        print(f"错误: {e}") 