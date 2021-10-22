# strbind
strbind - lapidary text converter for translate an text file to the C-style string. My motivation is fast adding large text chunks to the C code

## Usage

Transform your text with ```python strbind.py --from=<Original file> --to=<Target file>```

List of possible arguments:
* **--from** - File with original content
* **--to** - Target file. Text will be written in the original file, when **--to** argument are not used
* **--arr** - To add ```const char``` array syntax. The argument value is array name
* **--def** - To add preprocessor definition syntax. The argument value is definition name
* **--end** - String end ('LF'/'lf' or 'CRLF'/'crlf'). 'LF' by default

## Examples
### Certificate definition
* Existing cert.pem file:
```txt
-----BEGIN CERTIFICATE-----
MIIB3DCCAYOgAwIBAgINAgPlfvU/k/2lCSGypjAKBggqhkjOPQQDAjBQMSQwIgYD
VQQLExtHbG9iYWxTaWduIEVDQyBSb290IENBIC0gUjQxEzARBgNVBAoTCkdsb2Jh
bFNpZ24xEzARBgNVBAMTCkdsb2JhbFNpZ24wHhcNMTIxMTEzMDAwMDAwWhcNMzgw
MTE5MDMxNDA3WjBQMSQwIgYDVQQLExtHbG9iYWxTaWduIEVDQyBSb290IENBIC0g
UjQxEzARBgNVBAoTCkdsb2JhbFNpZ24xEzARBgNVBAMTCkdsb2JhbFNpZ24wWTAT
BgcqhkjOPQIBBggqhkjOPQMBBwNCAAS4xnnTj2wlDp8uORkcA6SumuU5BwkWymOx
uYb4ilfBV85C+nOh92VC/x7BALJucw7/xyHlGKSq2XE/qNS5zowdo0IwQDAOBgNV
HQ8BAf8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUVLB7rUW44kB/
+wpu+74zyTyjhNUwCgYIKoZIzj0EAwIDRwAwRAIgIk90crlgr/HmnKAWBVBfw147
bmF0774BxL4YSFlhgjICICadVGNA3jdgUM/I2O2dgq43mLyjj0xMqTQrbO/7lZsm
-----END CERTIFICATE-----
```
* Transforming command: 
```python strbind.py --from=s3_cer_base64.cer --to=cert.h --def=CERTIFICATE_ROOT_CA```

* Target cert.h file:
```cpp
#define CERTIFICATE_ROOT_CA \
    "-----BEGIN CERTIFICATE-----\n" \
    "MIIB3DCCAYOgAwIBAgINAgPlfvU/k/2lCSGypjAKBggqhkjOPQQDAjBQMSQwIgYD\n" \
    "VQQLExtHbG9iYWxTaWduIEVDQyBSb290IENBIC0gUjQxEzARBgNVBAoTCkdsb2Jh\n" \
    "bFNpZ24xEzARBgNVBAMTCkdsb2JhbFNpZ24wHhcNMTIxMTEzMDAwMDAwWhcNMzgw\n" \
    "MTE5MDMxNDA3WjBQMSQwIgYDVQQLExtHbG9iYWxTaWduIEVDQyBSb290IENBIC0g\n" \
    "UjQxEzARBgNVBAoTCkdsb2JhbFNpZ24xEzARBgNVBAMTCkdsb2JhbFNpZ24wWTAT\n" \
    "BgcqhkjOPQIBBggqhkjOPQMBBwNCAAS4xnnTj2wlDp8uORkcA6SumuU5BwkWymOx\n" \
    "uYb4ilfBV85C+nOh92VC/x7BALJucw7/xyHlGKSq2XE/qNS5zowdo0IwQDAOBgNV\n" \
    "HQ8BAf8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUVLB7rUW44kB/\n" \
    "+wpu+74zyTyjhNUwCgYIKoZIzj0EAwIDRwAwRAIgIk90crlgr/HmnKAWBVBfw147\n" \
    "bmF0774BxL4YSFlhgjICICadVGNA3jdgUM/I2O2dgq43mLyjj0xMqTQrbO/7lZsm\n" \
    "-----END CERTIFICATE-----\n"
```
### Text array
* Existing lorem.txt file:
```txt
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc aliquam non sapien a rhoncus.
Curabitur hendrerit neque et sapien eleifend, vitae rutrum enim lacinia.
Aliquam non dui eget metus auctor porta. Ut volutpat dolor vitae rhoncus tristique.
Proin finibus tellus quam, suscipit molestie orci condimentum ac. Nullam et sem justo.
Maecenas nibh lectus, vehicula ut mollis ut, scelerisque eu felis. Nunc non cursus quam, et
```

* Transforming command: 
```python strbind.py --from=s3_cer_base64.cer --to=poem.h --arr=lorem_ipsum --end=crlf```

* Target poem.h file:
```cpp
const char lorem_ipsum[435] = 
{
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc aliquam non sapien a rhoncus.\r\n"
    "Curabitur hendrerit neque et sapien eleifend, vitae rutrum enim lacinia.\r\n"
    "Aliquam non dui eget metus auctor porta. Ut volutpat dolor vitae rhoncus tristique.\r\n"
    "Proin finibus tellus quam, suscipit molestie orci condimentum ac. Nullam et sem justo.\r\n"
    "Maecenas nibh lectus, vehicula ut mollis ut, scelerisque eu felis. Nunc non cursus quam, et.\r\n"
};
```