#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from .models import Shortly


def index(request, error=None):
    all_el = Shortly.objects.all()
    return render(
        request,
        'shortly_app/new_url.html',
        {'all_el': all_el, 'error': error}
    )


def new_url(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            link_in_db = Shortly.objects.get(url_target=url)
            url_id = link_in_db.url_id
        except Shortly.DoesNotExist:
            short = Shortly(
                url_target=url,
                click_count=0
            )
            short.save()
            url_id = Shortly.objects.get(url_target=url).url_id
        return redirect('/shortly/detail/{}'.format(url_id))
    return redirect('/shortly')


def follow_link(request, url_id):
    try:
        link = Shortly.objects.get(url_id=url_id)
    except Shortly.DoesNotExist:
        return redirect('/shortly/http404')
    link.click_count += 1
    link.save()
    return redirect('{}'.format(link.url_target))


def link_detail(request, url_id):
    try:
        link_in_db = Shortly.objects.get(url_id=url_id)
    except Shortly.DoesNotExist:
        return redirect('/shortly/http404')
    return render(
        request,
        'shortly_app/short_link_details.html',
        {'link': link_in_db}
    )


def http404(request):
    return render(
        request,
        'shortly_app/404.html'
    )
