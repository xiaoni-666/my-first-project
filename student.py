import statistics # 用于计算标准差 (你之前问过的概念哦)

class GradeManager:
    def __init__(self):
        # 使用字典来存储学生数据：格式为 {'姓名': 分数}
        self.students = {}

    def add_student(self, name, score):
        """添加单个学生成绩"""
        self.students[name] = score

    def input_scores(self):
        """通过控制台循环录入成绩"""
        print("\n--- 📝 录入学生成绩 ---")
        print("输入格式：姓名 分数 (例如：张三 85)")
        print("提示：直接按回车(Enter)结束录入")
        
        while True:
            user_input = input("请输入: ").strip()
            if not user_input: # 如果直接回车，退出录入
                break
            
            parts = user_input.split()
            if len(parts) != 2:
                print("❌ 格式错误！请用空格隔开姓名和分数。")
                continue
                
            name, score_str = parts
            try:
                score = float(score_str)
                if score < 0 or score > 100:
                    print("❌ 分数必须在 0 到 100 之间！")
                    continue
                self.add_student(name, score)
                print(f"✅ 已添加：{name} - {score}分")
            except ValueError:
                print("❌ 分数必须是数字！")

    def show_statistics(self):
        """计算并展示统计数据"""
        if not self.students:
            print("\n⚠️ 当前没有学生数据，请先录入！")
            return

        print("\n--- 📊 成绩统计分析 ---")
        scores = list(self.students.values())
        names = list(self.students.keys())
        
        # 1. 基础数据统计
        total_students = len(scores)
        avg_score = sum(scores) / total_students
        max_score = max(scores)
        min_score = min(scores)
        std_dev = statistics.stdev(scores) if total_students > 1 else 0.0 # 样本标准差 (需要至少2个数据)
        
        # 2. 找出最高分和最低分对应的人 (可能会有同分并列)
        max_names = [name for name, score in self.students.items() if score == max_score]
        min_names = [name for name, score in self.students.items() if score == min_score]

        print(f"👨‍🎓 总人数: {total_students} 人")
        print(f"📈 平均分: {avg_score:.2f}")
        print(f"🔺 最高分: {max_score} (由 {', '.join(max_names)} 取得)")
        print(f"🔻 最低分: {min_score} (由 {', '.join(min_names)} 取得)")
        print(f"📉 标准差: {std_dev:.2f}")

    def show_sorted_scores(self):
        """按成绩从高到低排序显示"""
        if not self.students:
            print("\n⚠️ 当前没有学生数据！")
            return
            
        print("\n--- 📋 成绩排名 (从高到低) ---")
        # 使用 sorted 函数，配合 lambda 表达式按字典的 value (分数) 降序排序
        sorted_students = sorted(self.students.items(), key=lambda item: item[1], reverse=True)
        
        print(f"{'排名':<6}{'姓名':<10}{'分数':<10}")
        print("-" * 26)
        for rank, (name, score) in enumerate(sorted_students, 1):
            # 前三名加个小奖牌
            medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "  "
            print(f"{rank:<6}{name:<10}{score:<10} {medal}")

    def run(self):
        """主运行逻辑：交互菜单"""
        while True:
            print("\n" + "="*30)
            print("🎓 学生成绩管理系统 V1.0")
            print("="*30)
            print("1. 录入成绩")
            print("2. 查看统计结果")
            print("3. 查看成绩排名")
            print("0. 退出程序")
            print("="*30)
            
            choice = input("请选择功能 (0-3): ").strip()
            
            if choice == '1':
                self.input_scores()
            elif choice == '2':
                self.show_statistics()
            elif choice == '3':
                self.show_sorted_scores()
            elif choice == '0':
                print("👋 感谢使用，再见！")
                break
            else:
                print("❌ 无效输入，请重新选择！")

# ==========================================
# 程序入口
# ==========================================
if __name__ == "__main__":
    app = GradeManager()
    app.run()