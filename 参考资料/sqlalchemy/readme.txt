ѧԱ����ϵͳ��
�û���ɫ��ѧԱ/��ʦ�����ݵ�¼�Ľ�ɫ��ͬ�����������鲻ͬ��
��ʦ��ͼ��
1.����༶���ɴ����༶��insert  class_info into
			insert course_info into 
			commit
2.����ѧԱqq�Ű�ѧԱ����༶
	
3.�ɴ���ָ���༶���Ͽμ�¼��ע��һ���Ͽμ�¼��Ӧ����ѧԱ���Ͽμ�¼����ÿ�ڿζ�������ѧԱ�ϣ�Ϊ�˼�¼ÿλѧԱ��ѧϰ�ɼ�����Ҫ�ڴ���ÿ�ڿ��Ͽμ�¼��ͬʱ��Ϊ�������ѧԱ����һ���Ͽμ�¼��ΪѧԱ���ĳɼ���һ��һ���ֶ��޸ļ�¼


ѧԱ��ͼ��

1.�ύ��ҵ     
a.�ж��Ƿ��Ѿ��ύ�� finished = False
b.��ӡ���ύ����ҵ���û�ѡ����ҵ��
c.�������ݿ�
update course_detail set finished = True,learned = True where user_name = &student_name and course_id = & course_id 


2.�鿴��ҵ�ɼ� 
a.��ѯ�ɼ�
select * from user_grade where user_name = &student_name and course_id = & course_id
b.������ͼ��������
c.��ӡ�ɼ�������


һ��ѧԱ����ͬʱ���ڶ���༶������LinuxҲ���Ա�python
�ύ��ҵʱ��Ҫ��ѡ��༶����ѡ������ϿεĽ���
���ӣ�
ѧԱ���Բ鿴�Լ��İ༶�ɼ�����



һ���������
1.���ݿ����
user_info �� 
��    user_name   passwd   role	      qq_num	course_name  qq_group_num
����  �û���      ����     ��ɫ	  	qq��	�γ���	      һ����Ⱥ����

class_info��
class_name	user_name	                        teacher_name
�༶��		�û���(���user_info.user_name)		  ��ʦ��

course_info
course_name	course_id					            course_date	  class_name	      housework_name
�γ���		�γ̺ţ�����Ψһָ�����������ϿΣ�		�γ�����	  �����༶��(���class_info.class_name)	  �ÿγ̵���ҵ��

course_detail ��ϸ�Ŀγ̼�¼��ÿ��ÿ���Ͽεļ�¼
�� user_name course_id                               class_name           housework_name       finished			             learned 	    grade
   �û���     �γ̺ţ����course_info.course_id��      �༶��  		        ��ҵ��	      �Ƿ������ҵTrue/False	    ��ǩ��True/False	�ɼ�



