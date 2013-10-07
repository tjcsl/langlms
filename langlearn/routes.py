import langlearn
from langlearn.views import *


def add_view(url, function):
    langlearn.app.add_url_rule(
        url,
        view_func=function,
        methods=["GET", "POST"]
        )


def add_views(views):
    for i in views:
        add_view(i, views[i])

add_views(
    {
        ## Add new views to the end of this list.
        '/': core.index,
        '/login/': auth.login,
        '/logout/': auth.logout,
        '/register/': auth.register,
        ##
        '/credits/': credits.render_credits,
        ##
        '/user/settings/': user.settings,
        ##
        '/class/create/': classes.create_class,
        '/class/overview/<int:cid>/': classes.class_overview,
        '/class/students/<int:cid>/': classes.edit_students,
        '/class/students/add/': classes.add_student,
        '/class/students/del/': classes.rm_student,
        '/class/roles/set/s/<int:cid>/<int:uid>/': classes.make_student,
        '/class/roles/set/t/<int:cid>/<int:uid>/': classes.make_teacher,
        ##
        '/news/post/<int:cid>/': news.create_newspost,
        '/news/delete/<int:postid>/': news.delete_newspost,
        ##
        '/admin/users/students/': admin.get_students,
        '/admin/users/teachers/': admin.get_teachers,
        '/admin/users/siteadmins/': admin.get_siteadmins,
        '/admin/users/setstudent/<int:uid>/': admin.set_user_student,
        '/admin/users/setteacher/<int:uid>/': admin.set_user_teacher,
        '/admin/classes/all/': admin.get_classes,
        '/admin/classes/noteacher/': admin.get_classes_no_teacher
        ##
        }
    )
