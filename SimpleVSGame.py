# 导入 random(随机数) 模块
import random

# 游戏设置初始化
role_01 = '百里玄策'
role_02 = '韩信'
# 显示欢迎信息
print('=' * 10, f'欢迎光临《{role_01}大战{role_02}》', '=' * 10)
# 身份选择
print('请选择你的身份：')
print(f'\t1.{role_01}')
print(f'\t2.{role_02}')
player_choose = input('请选择[1-2]：')
# 分割线
print('=' * 43)
# 根据玩家的选择显示玩家的身份信息
if player_choose == '1':
    print(f"你选择了-》{role_01}《-来进行游戏！")
elif player_choose == '2':
    print(f"没想到吧！还是-》{role_01}《- ")
else:
    print(f"输入有误！自动分配身份为-》{role_01}《-")
# 初始化玩家生命值及攻击力
player_life = 25
player_attack = 10
# 设置BOSS的生命值及攻击力
boss_life = 100
boss_attack = 5
# 分割线
print('=' * 43)
# 显示玩家生命值及攻击力
print(f'{role_01} ：生命值 -> {player_life}\t攻击力 -> {player_attack}')
# 由于玩家的选项需要重复出现，所以要将其写在循环里
while True:
    # 分割线
    print('=' * 43)
    # 显示游戏选项，游戏正式开始！
    print('请选择你要进行的操作：')
    print('\t1.练级')
    print('\t2.打BOSS')
    print('\t3.逃跑')
    game_choose = input('请选择[1-3]：')

    # 处理玩家选择
    if game_choose == '1':
        player_life += 20
        player_attack += 2
        # 分割线
        print('=' * 43)
        # 显示玩家生命值及攻击力
        print(f'恭喜你升级了！ {role_01} ：生命值 -> {player_life}\t攻击力 -> {player_attack}')
    elif game_choose == '2':
        flag = True
        while True:
            # 分割线
            print('=' * 43)
            # 玩家攻击BOSS
            # 设置玩家攻击力随机值
            player_random_attack = random.randint(0, player_attack)
            boss_life -= player_random_attack
            if player_random_attack == 0:
                print(f'-》{role_01}《- 对 -》{role_02}《- 攻击无效')
            else:
                print(f'-》{role_01}《- 对 -》{role_02}《- 发起攻击')
                print(f'-》{role_02}《- 受到 {player_random_attack} 点攻击')
            # BOSS 死亡
            if boss_life <= 0:
                # 玩家胜利
                print(f'-》{role_02}《- 死亡！游戏结束！')
                flag = False
                break
            # BOSS反击
            # 设置BOSS攻击力随机值
            boss_random_attack = random.randint(0, boss_attack)
            player_life -= boss_random_attack
            if boss_random_attack == 0:
                print(f'-》{role_02}《- 对 -》{role_01}《- 攻击无效')
            else:
                print(f'-》{role_02}《- 对 -》{role_01}《- 发起攻击')
                print(f'-》{role_01}《- 受到 {boss_random_attack} 点攻击')
            # 玩家 死亡
            if player_life <= 0:
                # BOSS 胜利
                print(f' -》{role_01}《- 死亡！游戏结束！')
                flag = False
                break
        if not flag:
            break
    elif game_choose == '3':
        # 分割线
        print('=' * 43)
        print(f'-》{role_01}《- 察觉不妙，撒腿就跑！')
        break
    else:
        # 分割线
        print('=' * 43)
        print('输入无效，请重新输入')
