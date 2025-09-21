#!/usr/bin/env python3

import sys

BASE_AMOUNT = 831700
CHILD_ADD_FIRST_SECOND = 239300
CHILD_ADD_THIRD_PLUS = 79800

def calc_izoku_kiso_nenkin(num_children: int, has_spouse: bool) -> int:
    """
    遺族基礎年金の受給額を計算する
    :param num_children: 子どもの人数
    :param has_spouse: 配偶者がいるかどうか
    :return: 年額（円）
    """
    if num_children == 0:
        # 子がいないと遺族基礎年金は支給されない
        return 0

    if not has_spouse:
        # 子が受給する場合 → （基本額 + 第2子以降の加算）÷ 子の人数
        add_amount = 0
        if num_children >= 2:
            add_amount += CHILD_ADD_FIRST_SECOND
        if num_children >= 3:
            add_amount += CHILD_ADD_THIRD_PLUS * (num_children - 2)

        total = BASE_AMOUNT + add_amount
        return total // num_children  # 子の人数で均等割

    # 配偶者が受給する場合
    amount = BASE_AMOUNT

    if num_children >= 1:
        amount += CHILD_ADD_FIRST_SECOND
    if num_children >= 2:
        amount += CHILD_ADD_FIRST_SECOND
    if num_children >= 3:
        amount += CHILD_ADD_THIRD_PLUS * (num_children - 2)

    return amount


def main():
    print("=== 遺族基礎年金 受給額計算ツール ===")

    try:
        spouse_input = input("配偶者はいますか？ (y/n): ").strip().lower()
        num_children = int(input("子どもの人数を入力してください: "))
        has_spouse = spouse_input == "y"
    except Exception as e:
        print("入力エラー:", e)
        sys.exit(1)

    amount = calc_izoku_kiso_nenkin(num_children, has_spouse)

    if amount == 0:
        print("\n👉 子どもがいない場合は遺族基礎年金は支給されません。")
    else:
        print(f"\n👉 年額の受給額は {amount:,} 円 です。")


if __name__ == "__main__":
    main()
