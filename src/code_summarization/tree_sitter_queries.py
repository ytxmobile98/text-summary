JAVA_QUERY = """
; 顶级结构
(package_declaration (scoped_identifier) @package)

; 类和接口
(class_declaration
    (modifiers)? @modifiers
    name: (identifier) @class_name
)

; 顶级枚举
; 我们只捕获枚举的名称，不进入其内部捕获常量
(enum_declaration
    (modifiers)? @modifiers
    name: (identifier) @enum_name
    body: (enum_body) @enum_body_node
)

; 构造函数
(constructor_declaration
    (modifiers)? @modifiers
    name: (identifier) @method_constructor
    parameters: (formal_parameters) @method_params
)

; 方法/函数
(method_declaration
    (modifiers)? @modifiers
    type: (_unannotated_type) @method_return_type
    name: (identifier) @method_name
    parameters: (formal_parameters) @method_params
)
"""
