#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {response.status_code}')

    if response.status_code == 200:
        data = response.json()
        for dd in data:
            print(dd['title'])


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        with open('posts.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            fields = ['id', 'title', 'body']

            writer.writerow(fields)
            data = response.json()
            for dd in data:
                writer.writerow([
                    dd['id'],
                    dd['title'],
                    dd['body']
                ])
