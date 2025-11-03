JAVA_QUERY = """
; 顶级结构
(package_declaration (scoped_identifier) @package)

; 类和接口
(class_declaration
    (
        (modifiers)?
        name: (identifier)
    ) @class
)

; 顶级枚举
; 我们只捕获枚举的名称，不进入其内部捕获常量
(enum_declaration
    (
        (modifiers)?
        name: (identifier)
        body: (enum_body)
    ) @enum
)

; 构造函数
(constructor_declaration
    _+ @constructor
    (constructor_body)
)

; 方法/函数
(method_declaration
    _+ @method
    [
        (block)
        ";"
    ]
)
"""
