# /src/views/BlogpostView.py
from flask import request, g, Blueprint, json, Response
from marshmallow import ValidationError

from ..shared.Authentication import Auth
from ..models.BlogPostModel import BlogPostModel, BlogPostSchema

blogpost_api = Blueprint('blogpost_api', __name__)
blogpost_schema = BlogPostSchema()


@blogpost_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
    """
    Create Blogpost Function
    """
    req_data = request.get_json()
    req_data['owner_id'] = g.user.get('id')

    try:
        data = blogpost_schema.load(req_data)
    except ValidationError as error:
        if error:
            return custom_response(error, 400)

    post = BlogPostModel(data)
    post.save()
    data = blogpost_schema.dump(post)
    return custom_response(data, 201)


@blogpost_api.route('/', methods=['GET'])
def get_all():
    """
    Get All Blogposts
    """
    posts = BlogPostModel.get_all_blogposts()
    data = blogpost_schema.dump(posts, many=True)
    return custom_response(data, 200)


@blogpost_api.route('/<int:blogpost_id>', methods=['GET'])
def get_one(blogpost_id):
    """
    Get A Blogpost
    """
    post = BlogPostModel.get_one_blogpost(blogpost_id)
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    data = blogpost_schema.dump(post)
    return custom_response(data, 200)


@blogpost_api.route('/<int:blogpost_id>', methods=['PUT'])
@Auth.auth_required
def update(blogpost_id):
    """
    Update A Blogpost
    """
    req_data = request.get_json()
    post = BlogPostModel.get_one_blogpost(blogpost_id)
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    data = blogpost_schema.dump(post)
    if data.get('owner_id') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    try:
        data = blogpost_schema.load(req_data, partial=True)
    except ValidationError as error:
        if error:
            return custom_response(error, 400)

    post.update(data)

    data = blogpost_schema.dump(post)
    return custom_response(data, 200)


@blogpost_api.route('/<int:blogpost_id>', methods=['DELETE'])
@Auth.auth_required
def delete(blogpost_id):
    """
    Delete A BlogPost
    """
    post = BlogPostModel.get_one_blogpost(blogpost_id)
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    data = blogpost_schema.dump(post)
    if data.get('owner_id') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    post.delete()
    return custom_response({'message': 'deleted'}, 204)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
