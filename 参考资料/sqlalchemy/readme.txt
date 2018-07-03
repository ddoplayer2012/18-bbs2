学员管理系统：
用户角色：学员/讲师，根据登录的角色不同，能做的事情不同，
讲师视图：
1.管理班级，可创建班级，insert  class_info into
			insert course_info into 
			commit
2.根据学员qq号把学员加入班级
	
3.可创建指定班级的上课记录，注意一节上课记录对应多条学员的上课记录，即每节课都有整班学员上，为了记录每位学员的学习成绩，需要在创建每节课上课记录的同时，为整个班的学员创建一条上课记录，为学员批改成绩，一条一条手动修改记录


学员视图：

1.提交作业     
a.判断是否已经提交过 finished = False
b.打印可提交的作业，用户选择作业号
c.更新数据库
update course_detail set finished = True,learned = True where user_name = &student_name and course_id = & course_id 


2.查看作业成绩 
a.查询成绩
select * from user_grade where user_name = &student_name and course_id = & course_id
b.根据视图计算排名
c.打印成绩和排名


一个学员可以同时属于多个班级，报了Linux也可以报python
提交作业时需要先选择班级，再选择具体上课的节数
附加：
学员可以查看自己的班级成绩排名



一、需求分析
1.数据库设计
user_info 表 
列    user_name   passwd   role	      qq_num	course_name  qq_group_num
解释  用户名      密码     角色	  	qq号	课程名	      一键拉群进组

class_info表
class_name	user_name	                        teacher_name
班级名		用户名(外键user_info.user_name)		  讲师名

course_info
course_name	course_id					            course_date	  class_name	      housework_name
课程名		课程号（主键唯一指定任意日期上课）		课程日期	  关联班级名(外键class_info.class_name)	  该课程的作业名

course_detail 详细的课程记录，每人每次上课的记录
列 user_name course_id                               class_name           housework_name       finished			             learned 	    grade
   用户名     课程号（外键course_info.course_id）      班级名  		        作业名	      是否完成作业True/False	    已签到True/False	成绩



