GET http://127.0.0.1:5000/
return info


POST http://127.0.0.1:5000/login
registered new user
Example:
{
	"username": "el",
	"password": "qwe",
	"confirm_password": "qwe"
}


GET http://127.0.0.1:5000/api/board/
return board


POST http://127.0.0.1:5000/api/add_advert/
add new advert
Example:
{
	"advert_name": "1 ad trololo"
}


GET http://127.0.0.1:5000/api/advert/<advert_id>
show detail view about board, comments, likes
Example:


POST http://127.0.0.1:5000/api/advert/<advert_id>/add_comment/
add new comment for advert
Example:
{
	"comment": "ad1 com1 ulala"
}


GET http://127.0.0.1:5000/api/advert/<advert_id>/add_like/
add new like for advert
