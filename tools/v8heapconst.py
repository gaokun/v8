# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  64: "SYMBOL_TYPE",
  65: "HEAP_NUMBER_TYPE",
  66: "BIGINT_TYPE",
  67: "ODDBALL_TYPE",
  68: "MAP_TYPE",
  69: "CODE_TYPE",
  70: "MUTABLE_HEAP_NUMBER_TYPE",
  71: "FOREIGN_TYPE",
  72: "BYTE_ARRAY_TYPE",
  73: "BYTECODE_ARRAY_TYPE",
  74: "FREE_SPACE_TYPE",
  75: "FIXED_INT8_ARRAY_TYPE",
  76: "FIXED_UINT8_ARRAY_TYPE",
  77: "FIXED_INT16_ARRAY_TYPE",
  78: "FIXED_UINT16_ARRAY_TYPE",
  79: "FIXED_INT32_ARRAY_TYPE",
  80: "FIXED_UINT32_ARRAY_TYPE",
  81: "FIXED_FLOAT32_ARRAY_TYPE",
  82: "FIXED_FLOAT64_ARRAY_TYPE",
  83: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  84: "FIXED_BIGINT64_ARRAY_TYPE",
  85: "FIXED_BIGUINT64_ARRAY_TYPE",
  86: "FIXED_DOUBLE_ARRAY_TYPE",
  87: "FEEDBACK_METADATA_TYPE",
  88: "FILLER_TYPE",
  89: "ACCESS_CHECK_INFO_TYPE",
  90: "ACCESSOR_INFO_TYPE",
  91: "ACCESSOR_PAIR_TYPE",
  92: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  93: "ALLOCATION_MEMENTO_TYPE",
  94: "ASM_WASM_DATA_TYPE",
  95: "ASYNC_GENERATOR_REQUEST_TYPE",
  96: "CLASS_POSITIONS_TYPE",
  97: "DEBUG_INFO_TYPE",
  98: "FUNCTION_TEMPLATE_INFO_TYPE",
  99: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  100: "INTERCEPTOR_INFO_TYPE",
  101: "INTERPRETER_DATA_TYPE",
  102: "MODULE_INFO_ENTRY_TYPE",
  103: "MODULE_TYPE",
  104: "OBJECT_TEMPLATE_INFO_TYPE",
  105: "PROMISE_CAPABILITY_TYPE",
  106: "PROMISE_REACTION_TYPE",
  107: "PROTOTYPE_INFO_TYPE",
  108: "SCRIPT_TYPE",
  109: "STACK_FRAME_INFO_TYPE",
  110: "STACK_TRACE_FRAME_TYPE",
  111: "TUPLE2_TYPE",
  112: "TUPLE3_TYPE",
  113: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  114: "WASM_DEBUG_INFO_TYPE",
  115: "WASM_EXCEPTION_TAG_TYPE",
  116: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  117: "CALLABLE_TASK_TYPE",
  118: "CALLBACK_TASK_TYPE",
  119: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  120: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  121: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  122: "FINALIZATION_GROUP_CLEANUP_JOB_TASK_TYPE",
  123: "ALLOCATION_SITE_TYPE",
  124: "EMBEDDER_DATA_ARRAY_TYPE",
  125: "FIXED_ARRAY_TYPE",
  126: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  127: "HASH_TABLE_TYPE",
  128: "ORDERED_HASH_MAP_TYPE",
  129: "ORDERED_HASH_SET_TYPE",
  130: "ORDERED_NAME_DICTIONARY_TYPE",
  131: "NAME_DICTIONARY_TYPE",
  132: "GLOBAL_DICTIONARY_TYPE",
  133: "NUMBER_DICTIONARY_TYPE",
  134: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  135: "STRING_TABLE_TYPE",
  136: "EPHEMERON_HASH_TABLE_TYPE",
  137: "SCOPE_INFO_TYPE",
  138: "SCRIPT_CONTEXT_TABLE_TYPE",
  139: "AWAIT_CONTEXT_TYPE",
  140: "BLOCK_CONTEXT_TYPE",
  141: "CATCH_CONTEXT_TYPE",
  142: "DEBUG_EVALUATE_CONTEXT_TYPE",
  143: "EVAL_CONTEXT_TYPE",
  144: "FUNCTION_CONTEXT_TYPE",
  145: "MODULE_CONTEXT_TYPE",
  146: "NATIVE_CONTEXT_TYPE",
  147: "SCRIPT_CONTEXT_TYPE",
  148: "WITH_CONTEXT_TYPE",
  149: "WEAK_FIXED_ARRAY_TYPE",
  150: "TRANSITION_ARRAY_TYPE",
  151: "CALL_HANDLER_INFO_TYPE",
  152: "CELL_TYPE",
  153: "CODE_DATA_CONTAINER_TYPE",
  154: "DESCRIPTOR_ARRAY_TYPE",
  155: "FEEDBACK_CELL_TYPE",
  156: "FEEDBACK_VECTOR_TYPE",
  157: "LOAD_HANDLER_TYPE",
  158: "PREPARSE_DATA_TYPE",
  159: "PROPERTY_ARRAY_TYPE",
  160: "PROPERTY_CELL_TYPE",
  161: "SHARED_FUNCTION_INFO_TYPE",
  162: "SMALL_ORDERED_HASH_MAP_TYPE",
  163: "SMALL_ORDERED_HASH_SET_TYPE",
  164: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  165: "STORE_HANDLER_TYPE",
  166: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  167: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  168: "WEAK_ARRAY_LIST_TYPE",
  169: "WEAK_CELL_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1064: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1065: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1066: "JS_DATE_TYPE",
  1067: "JS_ERROR_TYPE",
  1068: "JS_GENERATOR_OBJECT_TYPE",
  1069: "JS_MAP_TYPE",
  1070: "JS_MAP_KEY_ITERATOR_TYPE",
  1071: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1072: "JS_MAP_VALUE_ITERATOR_TYPE",
  1073: "JS_MESSAGE_OBJECT_TYPE",
  1074: "JS_PROMISE_TYPE",
  1075: "JS_REGEXP_TYPE",
  1076: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1077: "JS_SET_TYPE",
  1078: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1079: "JS_SET_VALUE_ITERATOR_TYPE",
  1080: "JS_STRING_ITERATOR_TYPE",
  1081: "JS_WEAK_REF_TYPE",
  1082: "JS_FINALIZATION_GROUP_CLEANUP_ITERATOR_TYPE",
  1083: "JS_FINALIZATION_GROUP_TYPE",
  1084: "JS_WEAK_MAP_TYPE",
  1085: "JS_WEAK_SET_TYPE",
  1086: "JS_TYPED_ARRAY_TYPE",
  1087: "JS_DATA_VIEW_TYPE",
  1088: "JS_INTL_V8_BREAK_ITERATOR_TYPE",
  1089: "JS_INTL_COLLATOR_TYPE",
  1090: "JS_INTL_DATE_TIME_FORMAT_TYPE",
  1091: "JS_INTL_LIST_FORMAT_TYPE",
  1092: "JS_INTL_LOCALE_TYPE",
  1093: "JS_INTL_NUMBER_FORMAT_TYPE",
  1094: "JS_INTL_PLURAL_RULES_TYPE",
  1095: "JS_INTL_RELATIVE_TIME_FORMAT_TYPE",
  1096: "JS_INTL_SEGMENT_ITERATOR_TYPE",
  1097: "JS_INTL_SEGMENTER_TYPE",
  1098: "WASM_EXCEPTION_TYPE",
  1099: "WASM_GLOBAL_TYPE",
  1100: "WASM_INSTANCE_TYPE",
  1101: "WASM_MEMORY_TYPE",
  1102: "WASM_MODULE_TYPE",
  1103: "WASM_TABLE_TYPE",
  1104: "JS_BOUND_FUNCTION_TYPE",
  1105: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("RO_SPACE", 0x00139): (74, "FreeSpaceMap"),
  ("RO_SPACE", 0x00189): (68, "MetaMap"),
  ("RO_SPACE", 0x00209): (67, "NullMap"),
  ("RO_SPACE", 0x00271): (154, "DescriptorArrayMap"),
  ("RO_SPACE", 0x002d1): (149, "WeakFixedArrayMap"),
  ("RO_SPACE", 0x00321): (88, "OnePointerFillerMap"),
  ("RO_SPACE", 0x00371): (88, "TwoPointerFillerMap"),
  ("RO_SPACE", 0x003f1): (67, "UninitializedMap"),
  ("RO_SPACE", 0x00461): (8, "OneByteInternalizedStringMap"),
  ("RO_SPACE", 0x00501): (67, "UndefinedMap"),
  ("RO_SPACE", 0x00561): (65, "HeapNumberMap"),
  ("RO_SPACE", 0x005e1): (67, "TheHoleMap"),
  ("RO_SPACE", 0x00689): (67, "BooleanMap"),
  ("RO_SPACE", 0x00761): (72, "ByteArrayMap"),
  ("RO_SPACE", 0x007b1): (125, "FixedArrayMap"),
  ("RO_SPACE", 0x00801): (125, "FixedCOWArrayMap"),
  ("RO_SPACE", 0x00851): (127, "HashTableMap"),
  ("RO_SPACE", 0x008a1): (64, "SymbolMap"),
  ("RO_SPACE", 0x008f1): (40, "OneByteStringMap"),
  ("RO_SPACE", 0x00941): (137, "ScopeInfoMap"),
  ("RO_SPACE", 0x00991): (161, "SharedFunctionInfoMap"),
  ("RO_SPACE", 0x009e1): (69, "CodeMap"),
  ("RO_SPACE", 0x00a31): (144, "FunctionContextMap"),
  ("RO_SPACE", 0x00a81): (152, "CellMap"),
  ("RO_SPACE", 0x00ad1): (160, "GlobalPropertyCellMap"),
  ("RO_SPACE", 0x00b21): (71, "ForeignMap"),
  ("RO_SPACE", 0x00b71): (150, "TransitionArrayMap"),
  ("RO_SPACE", 0x00bc1): (156, "FeedbackVectorMap"),
  ("RO_SPACE", 0x00c61): (67, "ArgumentsMarkerMap"),
  ("RO_SPACE", 0x00d01): (67, "ExceptionMap"),
  ("RO_SPACE", 0x00da1): (67, "TerminationExceptionMap"),
  ("RO_SPACE", 0x00e49): (67, "OptimizedOutMap"),
  ("RO_SPACE", 0x00ee9): (67, "StaleRegisterMap"),
  ("RO_SPACE", 0x00f59): (146, "NativeContextMap"),
  ("RO_SPACE", 0x00fa9): (145, "ModuleContextMap"),
  ("RO_SPACE", 0x00ff9): (143, "EvalContextMap"),
  ("RO_SPACE", 0x01049): (147, "ScriptContextMap"),
  ("RO_SPACE", 0x01099): (139, "AwaitContextMap"),
  ("RO_SPACE", 0x010e9): (140, "BlockContextMap"),
  ("RO_SPACE", 0x01139): (141, "CatchContextMap"),
  ("RO_SPACE", 0x01189): (148, "WithContextMap"),
  ("RO_SPACE", 0x011d9): (142, "DebugEvaluateContextMap"),
  ("RO_SPACE", 0x01229): (138, "ScriptContextTableMap"),
  ("RO_SPACE", 0x01279): (87, "FeedbackMetadataArrayMap"),
  ("RO_SPACE", 0x012c9): (125, "ArrayListMap"),
  ("RO_SPACE", 0x01319): (66, "BigIntMap"),
  ("RO_SPACE", 0x01369): (126, "ObjectBoilerplateDescriptionMap"),
  ("RO_SPACE", 0x013b9): (73, "BytecodeArrayMap"),
  ("RO_SPACE", 0x01409): (153, "CodeDataContainerMap"),
  ("RO_SPACE", 0x01459): (86, "FixedDoubleArrayMap"),
  ("RO_SPACE", 0x014a9): (132, "GlobalDictionaryMap"),
  ("RO_SPACE", 0x014f9): (155, "ManyClosuresCellMap"),
  ("RO_SPACE", 0x01549): (125, "ModuleInfoMap"),
  ("RO_SPACE", 0x01599): (70, "MutableHeapNumberMap"),
  ("RO_SPACE", 0x015e9): (131, "NameDictionaryMap"),
  ("RO_SPACE", 0x01639): (155, "NoClosuresCellMap"),
  ("RO_SPACE", 0x01689): (133, "NumberDictionaryMap"),
  ("RO_SPACE", 0x016d9): (155, "OneClosureCellMap"),
  ("RO_SPACE", 0x01729): (128, "OrderedHashMapMap"),
  ("RO_SPACE", 0x01779): (129, "OrderedHashSetMap"),
  ("RO_SPACE", 0x017c9): (130, "OrderedNameDictionaryMap"),
  ("RO_SPACE", 0x01819): (158, "PreparseDataMap"),
  ("RO_SPACE", 0x01869): (159, "PropertyArrayMap"),
  ("RO_SPACE", 0x018b9): (151, "SideEffectCallHandlerInfoMap"),
  ("RO_SPACE", 0x01909): (151, "SideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x01959): (151, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x019a9): (134, "SimpleNumberDictionaryMap"),
  ("RO_SPACE", 0x019f9): (125, "SloppyArgumentsElementsMap"),
  ("RO_SPACE", 0x01a49): (162, "SmallOrderedHashMapMap"),
  ("RO_SPACE", 0x01a99): (163, "SmallOrderedHashSetMap"),
  ("RO_SPACE", 0x01ae9): (164, "SmallOrderedNameDictionaryMap"),
  ("RO_SPACE", 0x01b39): (135, "StringTableMap"),
  ("RO_SPACE", 0x01b89): (166, "UncompiledDataWithoutPreparseDataMap"),
  ("RO_SPACE", 0x01bd9): (167, "UncompiledDataWithPreparseDataMap"),
  ("RO_SPACE", 0x01c29): (168, "WeakArrayListMap"),
  ("RO_SPACE", 0x01c79): (136, "EphemeronHashTableMap"),
  ("RO_SPACE", 0x01cc9): (124, "EmbedderDataArrayMap"),
  ("RO_SPACE", 0x01d19): (169, "WeakCellMap"),
  ("RO_SPACE", 0x01d69): (58, "NativeSourceStringMap"),
  ("RO_SPACE", 0x01db9): (32, "StringMap"),
  ("RO_SPACE", 0x01e09): (41, "ConsOneByteStringMap"),
  ("RO_SPACE", 0x01e59): (33, "ConsStringMap"),
  ("RO_SPACE", 0x01ea9): (45, "ThinOneByteStringMap"),
  ("RO_SPACE", 0x01ef9): (37, "ThinStringMap"),
  ("RO_SPACE", 0x01f49): (35, "SlicedStringMap"),
  ("RO_SPACE", 0x01f99): (43, "SlicedOneByteStringMap"),
  ("RO_SPACE", 0x01fe9): (34, "ExternalStringMap"),
  ("RO_SPACE", 0x02039): (42, "ExternalOneByteStringMap"),
  ("RO_SPACE", 0x02089): (50, "UncachedExternalStringMap"),
  ("RO_SPACE", 0x020d9): (0, "InternalizedStringMap"),
  ("RO_SPACE", 0x02129): (2, "ExternalInternalizedStringMap"),
  ("RO_SPACE", 0x02179): (10, "ExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x021c9): (18, "UncachedExternalInternalizedStringMap"),
  ("RO_SPACE", 0x02219): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x02269): (58, "UncachedExternalOneByteStringMap"),
  ("RO_SPACE", 0x022b9): (76, "FixedUint8ArrayMap"),
  ("RO_SPACE", 0x02309): (75, "FixedInt8ArrayMap"),
  ("RO_SPACE", 0x02359): (78, "FixedUint16ArrayMap"),
  ("RO_SPACE", 0x023a9): (77, "FixedInt16ArrayMap"),
  ("RO_SPACE", 0x023f9): (80, "FixedUint32ArrayMap"),
  ("RO_SPACE", 0x02449): (79, "FixedInt32ArrayMap"),
  ("RO_SPACE", 0x02499): (81, "FixedFloat32ArrayMap"),
  ("RO_SPACE", 0x024e9): (82, "FixedFloat64ArrayMap"),
  ("RO_SPACE", 0x02539): (83, "FixedUint8ClampedArrayMap"),
  ("RO_SPACE", 0x02589): (85, "FixedBigUint64ArrayMap"),
  ("RO_SPACE", 0x025d9): (84, "FixedBigInt64ArrayMap"),
  ("RO_SPACE", 0x02629): (67, "SelfReferenceMarkerMap"),
  ("RO_SPACE", 0x02691): (111, "Tuple2Map"),
  ("RO_SPACE", 0x02731): (113, "ArrayBoilerplateDescriptionMap"),
  ("RO_SPACE", 0x02a71): (100, "InterceptorInfoMap"),
  ("RO_SPACE", 0x05059): (89, "AccessCheckInfoMap"),
  ("RO_SPACE", 0x050a9): (90, "AccessorInfoMap"),
  ("RO_SPACE", 0x050f9): (91, "AccessorPairMap"),
  ("RO_SPACE", 0x05149): (92, "AliasedArgumentsEntryMap"),
  ("RO_SPACE", 0x05199): (93, "AllocationMementoMap"),
  ("RO_SPACE", 0x051e9): (94, "AsmWasmDataMap"),
  ("RO_SPACE", 0x05239): (95, "AsyncGeneratorRequestMap"),
  ("RO_SPACE", 0x05289): (96, "ClassPositionsMap"),
  ("RO_SPACE", 0x052d9): (97, "DebugInfoMap"),
  ("RO_SPACE", 0x05329): (98, "FunctionTemplateInfoMap"),
  ("RO_SPACE", 0x05379): (99, "FunctionTemplateRareDataMap"),
  ("RO_SPACE", 0x053c9): (101, "InterpreterDataMap"),
  ("RO_SPACE", 0x05419): (102, "ModuleInfoEntryMap"),
  ("RO_SPACE", 0x05469): (103, "ModuleMap"),
  ("RO_SPACE", 0x054b9): (104, "ObjectTemplateInfoMap"),
  ("RO_SPACE", 0x05509): (105, "PromiseCapabilityMap"),
  ("RO_SPACE", 0x05559): (106, "PromiseReactionMap"),
  ("RO_SPACE", 0x055a9): (107, "PrototypeInfoMap"),
  ("RO_SPACE", 0x055f9): (108, "ScriptMap"),
  ("RO_SPACE", 0x05649): (109, "StackFrameInfoMap"),
  ("RO_SPACE", 0x05699): (110, "StackTraceFrameMap"),
  ("RO_SPACE", 0x056e9): (112, "Tuple3Map"),
  ("RO_SPACE", 0x05739): (114, "WasmDebugInfoMap"),
  ("RO_SPACE", 0x05789): (115, "WasmExceptionTagMap"),
  ("RO_SPACE", 0x057d9): (116, "WasmExportedFunctionDataMap"),
  ("RO_SPACE", 0x05829): (117, "CallableTaskMap"),
  ("RO_SPACE", 0x05879): (118, "CallbackTaskMap"),
  ("RO_SPACE", 0x058c9): (119, "PromiseFulfillReactionJobTaskMap"),
  ("RO_SPACE", 0x05919): (120, "PromiseRejectReactionJobTaskMap"),
  ("RO_SPACE", 0x05969): (121, "PromiseResolveThenableJobTaskMap"),
  ("RO_SPACE", 0x059b9): (122, "FinalizationGroupCleanupJobTaskMap"),
  ("RO_SPACE", 0x05a09): (123, "AllocationSiteWithWeakNextMap"),
  ("RO_SPACE", 0x05a59): (123, "AllocationSiteWithoutWeakNextMap"),
  ("RO_SPACE", 0x05aa9): (157, "LoadHandler1Map"),
  ("RO_SPACE", 0x05af9): (157, "LoadHandler2Map"),
  ("RO_SPACE", 0x05b49): (157, "LoadHandler3Map"),
  ("RO_SPACE", 0x05b99): (165, "StoreHandler0Map"),
  ("RO_SPACE", 0x05be9): (165, "StoreHandler1Map"),
  ("RO_SPACE", 0x05c39): (165, "StoreHandler2Map"),
  ("RO_SPACE", 0x05c89): (165, "StoreHandler3Map"),
  ("MAP_SPACE", 0x00139): (1057, "ExternalMap"),
  ("MAP_SPACE", 0x00189): (1073, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("RO_SPACE", 0x001d9): "NullValue",
  ("RO_SPACE", 0x00259): "EmptyDescriptorArray",
  ("RO_SPACE", 0x002c1): "EmptyWeakFixedArray",
  ("RO_SPACE", 0x003c1): "UninitializedValue",
  ("RO_SPACE", 0x004d1): "UndefinedValue",
  ("RO_SPACE", 0x00551): "NanValue",
  ("RO_SPACE", 0x005b1): "TheHoleValue",
  ("RO_SPACE", 0x00649): "HoleNanValue",
  ("RO_SPACE", 0x00659): "TrueValue",
  ("RO_SPACE", 0x00709): "FalseValue",
  ("RO_SPACE", 0x00751): "empty_string",
  ("RO_SPACE", 0x00c11): "EmptyScopeInfo",
  ("RO_SPACE", 0x00c21): "EmptyFixedArray",
  ("RO_SPACE", 0x00c31): "ArgumentsMarker",
  ("RO_SPACE", 0x00cd1): "Exception",
  ("RO_SPACE", 0x00d71): "TerminationException",
  ("RO_SPACE", 0x00e19): "OptimizedOut",
  ("RO_SPACE", 0x00eb9): "StaleRegister",
  ("RO_SPACE", 0x02679): "EmptyEnumCache",
  ("RO_SPACE", 0x026e1): "EmptyPropertyArray",
  ("RO_SPACE", 0x026f1): "EmptyByteArray",
  ("RO_SPACE", 0x02701): "EmptyObjectBoilerplateDescription",
  ("RO_SPACE", 0x02719): "EmptyArrayBoilerplateDescription",
  ("RO_SPACE", 0x02781): "EmptyFixedUint8Array",
  ("RO_SPACE", 0x027a1): "EmptyFixedInt8Array",
  ("RO_SPACE", 0x027c1): "EmptyFixedUint16Array",
  ("RO_SPACE", 0x027e1): "EmptyFixedInt16Array",
  ("RO_SPACE", 0x02801): "EmptyFixedUint32Array",
  ("RO_SPACE", 0x02821): "EmptyFixedInt32Array",
  ("RO_SPACE", 0x02841): "EmptyFixedFloat32Array",
  ("RO_SPACE", 0x02861): "EmptyFixedFloat64Array",
  ("RO_SPACE", 0x02881): "EmptyFixedUint8ClampedArray",
  ("RO_SPACE", 0x028a1): "EmptyFixedBigUint64Array",
  ("RO_SPACE", 0x028c1): "EmptyFixedBigInt64Array",
  ("RO_SPACE", 0x028e1): "EmptySloppyArgumentsElements",
  ("RO_SPACE", 0x02901): "EmptySlowElementDictionary",
  ("RO_SPACE", 0x02949): "EmptyOrderedHashMap",
  ("RO_SPACE", 0x02971): "EmptyOrderedHashSet",
  ("RO_SPACE", 0x02999): "EmptyFeedbackMetadata",
  ("RO_SPACE", 0x029a9): "EmptyPropertyCell",
  ("RO_SPACE", 0x029d1): "EmptyPropertyDictionary",
  ("RO_SPACE", 0x02a21): "NoOpInterceptorInfo",
  ("RO_SPACE", 0x02ac1): "EmptyWeakArrayList",
  ("RO_SPACE", 0x02ad9): "InfinityValue",
  ("RO_SPACE", 0x02ae9): "MinusZeroValue",
  ("RO_SPACE", 0x02af9): "MinusInfinityValue",
  ("RO_SPACE", 0x02b09): "SelfReferenceMarker",
  ("RO_SPACE", 0x02b61): "OffHeapTrampolineRelocationInfo",
  ("RO_SPACE", 0x02b79): "HashSeed",
  ("OLD_SPACE", 0x40139): "ArgumentsIteratorAccessor",
  ("OLD_SPACE", 0x401a9): "ArrayLengthAccessor",
  ("OLD_SPACE", 0x40219): "BoundFunctionLengthAccessor",
  ("OLD_SPACE", 0x40289): "BoundFunctionNameAccessor",
  ("OLD_SPACE", 0x402f9): "ErrorStackAccessor",
  ("OLD_SPACE", 0x40369): "FunctionArgumentsAccessor",
  ("OLD_SPACE", 0x403d9): "FunctionCallerAccessor",
  ("OLD_SPACE", 0x40449): "FunctionNameAccessor",
  ("OLD_SPACE", 0x404b9): "FunctionLengthAccessor",
  ("OLD_SPACE", 0x40529): "FunctionPrototypeAccessor",
  ("OLD_SPACE", 0x40599): "StringLengthAccessor",
  ("OLD_SPACE", 0x40609): "InvalidPrototypeValidityCell",
  ("OLD_SPACE", 0x40619): "EmptyScript",
  ("OLD_SPACE", 0x40699): "ManyClosuresCell",
  ("OLD_SPACE", 0x406a9): "ArrayConstructorProtector",
  ("OLD_SPACE", 0x406b9): "NoElementsProtector",
  ("OLD_SPACE", 0x406e1): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x406f1): "ArraySpeciesProtector",
  ("OLD_SPACE", 0x40719): "TypedArraySpeciesProtector",
  ("OLD_SPACE", 0x40741): "RegExpSpeciesProtector",
  ("OLD_SPACE", 0x40769): "PromiseSpeciesProtector",
  ("OLD_SPACE", 0x40791): "StringLengthProtector",
  ("OLD_SPACE", 0x407a1): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x407c9): "ArrayBufferDetachingProtector",
  ("OLD_SPACE", 0x407f1): "PromiseHookProtector",
  ("OLD_SPACE", 0x40819): "PromiseResolveProtector",
  ("OLD_SPACE", 0x40829): "MapIteratorProtector",
  ("OLD_SPACE", 0x40851): "PromiseThenProtector",
  ("OLD_SPACE", 0x40879): "SetIteratorProtector",
  ("OLD_SPACE", 0x408a1): "StringIteratorProtector",
  ("OLD_SPACE", 0x408c9): "SingleCharacterStringCache",
  ("OLD_SPACE", 0x410d9): "StringSplitCache",
  ("OLD_SPACE", 0x418e9): "RegExpMultipleCache",
  ("OLD_SPACE", 0x420f9): "BuiltinsConstantsTable",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
