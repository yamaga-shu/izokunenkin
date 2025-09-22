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

    base_amount = BASE_AMOUNT
    add_amount = 0

    # 子が受給する場合 → （基本額 + 第2子以降の加算）÷ 子の人数
    if not has_spouse:
        if num_children <= 2:
            add_amount = CHILD_ADD_FIRST_SECOND * num_children
        if num_children >= 3:
            add_amount = (CHILD_ADD_FIRST_SECOND * 2) + CHILD_ADD_THIRD_PLUS * (num_children - 2)

        total = base_amount + add_amount
        return total

    # 配偶者が受給する場合
    if num_children <= 2:
        add_amount = CHILD_ADD_FIRST_SECOND * num_children
    if num_children >= 3:
        add_amount = (CHILD_ADD_FIRST_SECOND * 2) + CHILD_ADD_THIRD_PLUS * (num_children - 2)

    total = base_amount + add_amount
    return total


def main():
    print("=== 遺族基礎年金 受給額計算ツール ===")

    try:
        spouse_input = input("配偶者はいますか？ (y/n): ").strip().lower()
        num_children = int(input("子どもの人数を入力してください: "))
        has_spouse = spouse_input == "y"
    except Exception as e:
        print("入力エラー:", e)
        sys.exit(1)

    # 受給額(年額)
    total = calc_izoku_kiso_nenkin(num_children, has_spouse)

    if total == 0:
        print("\n👉 子どもがいない場合は遺族基礎年金は支給されません。")
    else:
        # 受給額(月額)
        total_month = int(total / 12)
        print(f"\n👉 受給額は {total:,} (月額 {total_month:,}) 円です。")
        if not has_spouse:
            # 子ども一人当たり受給額
            per_child = int(total / num_children)
            per_child_month = int(per_child / 12)

            print(f"\n👦 子ども一人当たり {per_child:,} (月額 {per_child_month:,}) 円です。")

if __name__ == "__main__":
    main()
