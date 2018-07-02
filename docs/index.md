---
layout: default
---
<div class="post">
  <p>Now with htmls?</p>
  {{ content }}
  <ul>
    {% for post in site.posts %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>
</div>
