# HTTP Status Codes

## 1XX Informational
- **100 Continue**: The initial part of a request has been received and has not yet been rejected by the server.
- **101 Switching Protocols**: The requester has asked the server to switch protocols and the server is acknowledging that it will do so.

## 2XX Success
- **200 OK**: The request has succeeded. The meaning of the success depends on the HTTP method used.
- **201 Created**: The request has been fulfilled and has resulted in one or more new resources being created.
- **202 Accepted**: The request has been accepted for processing, but the processing has not been completed. The request might or might not eventually be acted upon.
- **203 Non-Authoritative Information**: The server is a transforming proxy that received a 200 OK from its origin, but is returning a modified version of the origin's response.
- **204 No Content**: The server successfully processed the request, but is not returning any content.
- **205 Reset Content**: The server successfully processed the request, but is not returning any content and requires that the requester reset the document view.
- **206 Partial Content**: The server is delivering only part of the resource due to a range header sent by the client.

## 3XX Redirection
- **300 Multiple Choices**: The request has more than one possible response. The user-agent or user should choose one of them.
- **301 Moved Permanently**: The URL of the requested resource has been changed permanently. The new URL is given in the response.
- **302 Found**: The requested resource resides temporarily under a different URL. The user-agent should use the original URL for future requests.
- **303 See Other**: The response to the request can be found under a different URL and should be retrieved using a GET method on that resource.
- **304 Not Modified**: Indicates that the resource has not been modified since the version specified by the request headers. The server does not return any body in the response.
- **305 Use Proxy**: The requested resource is available only through a proxy, the address for which is provided in the response. Many HTTP clients do not support this status code.
- **307 Temporary Redirect**: The requested resource resides temporarily under a different URL. The user-agent should use the original URL for future requests. This status code is similar to 302 Found, except that it does not allow the HTTP method to change. For example, a POST request must be repeated using another POST request.
- **308 Permanent Redirect**: The requested resource has been assigned a new permanent URI and any future references to this resource should use one of the returned URIs. This status code is similar to 301 Moved Permanently, except that it does not allow the HTTP method to change.

## 4XX Client Error
- **400 Bad Request**: The server cannot or will not process the request due to an apparent client error (e.g., malformed request syntax, size too large, invalid request message framing, or deceptive request routing).
- **401 Unauthorized**: The request has not been applied because it lacks valid authentication credentials for the target resource.
- **402 Payment Required**: Reserved for future use.
- **403 Forbidden**: The server understood the request but refuses to authorize it.
- **404 Not Found**: The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible.
- **405 Method Not Allowed**: A request method is not supported for the requested resource. For example, a GET request on a form that requires data to be presented via POST, or a PUT request on a read-only resource.
- **406 Not Acceptable**: The requested resource is capable of generating only content not acceptable according to the Accept headers sent in the request.
- **407 Proxy Authentication Required**: The client must first authenticate itself with the proxy.
- **408 Request Timeout**: The server timed out waiting for the request. According to HTTP specifications, the client did not produce a request within the time that the server was prepared to wait. The client may repeat the request without modifications at any later time.
- **409 Conflict**: Indicates that the request could not be processed because of conflict in the request, such as an edit conflict between multiple simultaneous updates.
- **410 Gone**: Indicates that the resource requested is no longer available and will not be available again. This should be used when a resource has been intentionally removed and the resource should be purged. Upon receiving a 410 status code, the client should not request the resource in the future. Clients such as search engines should remove the resource from their indices. Most use cases do not require clients and search engines to purge the resource, and a "404 Not Found" may be used instead.
- **411 Length Required**: The request did not specify the length of its content, which is required by the requested resource.
- **412 Precondition Failed**: The server does not meet one of the preconditions that the requester put on the request.
- **413 Payload Too Large**: The request is larger than the server is willing or able to process. Previously called "Request Entity Too Large".
- **414 URI Too Long**: The URI provided was too long for the server to process.
- **415 Unsupported Media Type**: The request entity has a media type which the server or resource does not support. For example, the client uploads an image as image/svg+xml, but the server requires that images use a different format.
- **416 Range Not Satisfiable**: The client has asked for a portion of the file (byte serving), but the server cannot supply that portion. For example, if the client asked for a part of the file that lies beyond the end of the file.
- **417 Expectation Failed**: The server cannot meet the requirements of the Expect request-header field.
- **418 I'm a teapot**: This code was defined in 1998 as one of the traditional IETF April Fools' jokes, in RFC 2324, Hyper Text Coffee Pot Control Protocol, and is not expected to be implemented by actual HTTP servers. The RFC specifies that any attempt to brew coffee with a teapot should result in the error code "418 I'm a teapot". This code is not a part of the HTTP standard, but is used by some websites as an Easter egg. The code is a reference to the 1998 April Fools' joke, and is not expected to be implemented by actual HTTP servers. The RFC specifies that any attempt to brew coffee with a teapot should result in the error code "418 I'm a teapot".
- **421 Misdirected Request**: The request was directed at a server that is not able to produce a response. This can be sent by a server that is not configured to produce responses for the combination of scheme and authority that are included in the request URI.
- **422 Unprocessable Entity**: The request was well-formed but was unable to be followed due to semantic errors.
- **423 Locked**: The resource that is being accessed is locked.
- **424 Failed Dependency**: The request failed due to failure of a previous request (e.g., a PROPPATCH).
- **425 Too Early**: Indicates that the server is unwilling to risk processing a request that might be replayed.
- **426 Upgrade Required**: The client should switch to a different protocol such as TLS/1.0, given in the Upgrade header field.
- **428 Precondition Required**: The origin server requires the request to be conditional. Intended to prevent the 'lost update' problem, where a client GETs a resource's state, modifies it, and PUTs it back to the server, when meanwhile a third party has modified the state on the server, leading to a conflict.
- **429 Too Many Requests**: The user has sent too many requests in a given amount of time ("rate limiting").
- **431 Request Header Fields   Too Large**: The server is unwilling to process the request because its header fields are too large. The request may be resubmitted after reducing the size of the request header fields.
- **451 Unavailable For Legal Reasons**: The user-agent requested a resource that cannot legally be provided, such as a web page censored by a government.

## 5XX Server Error
- **500 Internal Server Error**: The server has encountered a situation it doesn't know how to handle.
- **501 Not Implemented**: The request method is not supported by the server and cannot be handled. The only methods        
- **502 Bad Gateway**: The server, while acting as a gateway or proxy, received an invalid response from the upstream server.
- **503 Service Unavailable**: The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. Note that together with this response, a user-friendly page explaining the problem should be sent. This response should be used for temporary conditions and the Retry-After: HTTP header should, if possible, contain the estimated time before the recovery of the service. The webmaster must also take care to ensure that this response is not cached by the browser (or any other cache) to prevent the next request from being blocked for a long time.
- **504 Gateway Timeout**: The server was acting as a gateway or proxy and did not receive a timely response from the upstream server.
- **505 HTTP Version Not Supported**: The server does not support the HTTP protocol version used in the request.    
- **506 Variant Also Negotiates**: The server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process.
- **507 Insufficient Storage**: The server is unable to store the representation needed to complete the request. This condition is considered to be temporary. If the request that received this status code was the result of a user action, the request should be repeated after performing the appropriate action.
- **508 Loop Detected**: The server detected an infinite loop while processing a request with "Depth: infinity". This status indicates that the entire operation failed.
- **510 Not Extended**: Further extensions to the request are required for the server to fulfill it.
- **511 Network Authentication Required**: The client needs to authenticate to gain network access. This status is not widely used and is primarily intended for use by intercepting proxies used to control access to the network (e.g., "captive portals" used to require agreement to Terms of Service before granting full Internet access via a Wi-Fi hotspot).
## References
- [MDN Web Docs - HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [Wikipedia - List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
- [HTTP Status Codes](https://httpstatuses.com/)    
- [HTTP Status Codes - REST API Tutorial](https://restfulapi.net/http-status-codes/)    
- [HTTP Status Codes - W3C](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)
- [HTTP Status Codes - IETF](https://www.ietf.org/rfc/rfc7231.txt)
- [HTTP Status Codes - IANA](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)