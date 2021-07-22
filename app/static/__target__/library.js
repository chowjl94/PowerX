// Transcrypt'ed from Python, 2021-07-22 11:50:30
var random = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_random__ from './random.js';
__nest__ (random, '', __module_random__);
var __name__ = '__main__';
export var array = [];
export var gen_random_int = function (number, seed) {
	var result = null;
	var result = list (range (number));
	random.seed (seed);
	random.shuffle (result);
	return result;
};
export var array_to_str = function (array) {
	var a_str = '';
	for (var item of array) {
		var a_str = (a_str + ',') + str (item);
	}
	var a_str = a_str.__getslice__ (1, null, 1) + '.';
	return a_str;
};
export var generate = function () {
	var number = 10;
	var seed = 200;
	array = gen_random_int (number, seed);
	var array_str = array_to_str (array);
	document.getElementById ('generate').innerHTML = array_str;
};
export var insertion_sort = function (array) {
	for (var out = 1; out < len (array); out++) {
		var inn = out;
		var temp = array [inn];
		while (inn > 0 && temp < array [inn - 1]) {
			array [inn] = array [inn - 1];
			inn--;
		}
		array [inn] = temp;
	}
	return array;
};
export var sortnumber1 = function () {
	var new_list = array;
	var new_sort = insertion_sort (new_list);
	var array_str = array_to_str (new_sort);
	document.getElementById ('sorted').innerHTML = array_str;
};
export var sortnumber2 = function () {
	var value = document.getElementsByName ('numbers').value;
	if (value == '') {
		window.alert ('Your textbox is empty');
		return ;
	}
	var str_list = value.py_split (',');
	var num_list = list (map (int, str_list));
	var new_sort = insertion_sort (num_list);
	var array_str = str (new_sort);
	document.getElementById ('sorted').innerHTML = array_str;
};

//# sourceMappingURL=library.map