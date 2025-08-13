**Varnish Configuration Language (VCL)** is a domain-specific language used to define the behavior of the [Varnish Cache](https://varnish-cache.org/) HTTP accelerator. VCL lets you customize how Varnish handles HTTP requests, caching, backend selection, and much more.

---

### 🔧 Key Concepts of VCL

#### 1. **VCL Files**

VCL scripts usually have a `.vcl` extension. You write your logic in these files and load them into the Varnish daemon.

#### 2. **Subroutines**

VCL is built around *subroutines* (entry points) that Varnish calls at different stages of a request lifecycle. The most common ones include:

* `vcl_recv`: Called when a request is received.
* `vcl_backend_fetch`: Called before a request is sent to the backend.
* `vcl_backend_response`: Called after the backend response is received.
* `vcl_deliver`: Called before delivering a response to the client.
* `vcl_hit` / `vcl_miss`: Called depending on whether the content is in cache.

---

### 🧩 Basic VCL Example

```vcl
vcl 4.1;

backend default {
    .host = "127.0.0.1";
    .port = "8080";
}

sub vcl_recv {
    if (req.url ~ "^/admin") {
        return (pass);
    }
}

sub vcl_backend_response {
    if (beresp.status == 404) {
        set beresp.ttl = 10s;
    } else {
        set beresp.ttl = 5m;
    }
}

sub vcl_deliver {
    if (obj.hits > 0) {
        set resp.http.X-Cache = "HIT";
    } else {
        set resp.http.X-Cache = "MISS";
    }
}
```

---

### ⚙️ Common VCL Features

* **Backend definition**: Choose which backend server to use.
* **Caching control**: Override headers like `Cache-Control` or TTLs.
* **Custom headers**: Add debugging info, like `X-Cache: HIT/MISS`.
* **Edge-side includes (ESI)**: Used for caching part of a page.

---

### 🔒 Security Tip

Avoid caching dynamic pages or sensitive user data. Use conditions in `vcl_recv` like:

```vcl
if (req.http.Authorization || req.http.Cookie) {
    return (pass);
}
```

---

### 📚 Helpful Resources

* Official docs: [https://varnish-cache.org/docs/](https://varnish-cache.org/docs/)
* GitHub: [https://github.com/varnishcache/varnish-cache](https://github.com/varnishcache/varnish-cache)

Would you like a specific VCL example for a use case like WordPress, API caching, or load balancing?

