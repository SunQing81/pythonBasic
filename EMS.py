# 创建员工列表
emps = ['\t妲己\t18\t女', '\t韩信\t26\t男']
while True:
    # 显示首页信息
    print('-' * 20, '欢迎进入员工管理系统', '-' * 20)
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出系统')
    user_choose = input('请选择功能[1-4]：')
    # 插入分割线
    print('-' * 58)
    if user_choose == '1':
        # 查询所有员工信息
        # 定义员工序号
        n = 0
        print('序号\t姓名\t年龄\t性别')
        for s in emps:
            n += 1
            print(f'{n}{s}')
    elif user_choose == '2':
        # 添加员工
        name = input('请输入姓名：')
        age = input('请输入年龄：')
        gender = input('请输入性别：')
        empInfo = f'\t{name}\t{age}\t{gender}'
        print(empInfo)
        confirm = input('是否确认添加[y/n]：')
        if confirm == 'y':
            emps.append(empInfo)
            print('添加成功')
        else:
            print('添加失败')
    elif user_choose == '3':
        # 删除员工
        empNum = int(input('请输入员工序号：'))
        if 0 < empNum <= len(emps):
            empId = empNum - 1
            print(f'{empNum}{emps[empId]}')
            confirm = input('是否确认删除，且不可恢复[y/n]：')
            if confirm == 'y':
                emps.pop(empId)
                print('删除成功')
            else:
                print('删除失败')
            pass
    elif user_choose == '4':
        # 退出系统
        print('下次一定')
        input('按enter确认退出')
        break
    else:
        print('输入异常，请重新输入')
