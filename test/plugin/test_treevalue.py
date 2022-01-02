import pytest
from potc.testing import provement
from potc.translate import BlankTranslator
from treevalue import raw, TreeValue, FastTreeValue
from treevalue.tree.common import RawWrapper, create_storage, TreeStorage

from potc_treevalue.plugin import __rules__


@pytest.mark.unittest
class TestPlugin(provement(BlankTranslator(__rules__))):
    def test_treevalue_raw(self):
        with self.transobj_assert(raw({'a': 1, 'b': 2})) as (obj, name):
            assert isinstance(obj, RawWrapper)
            assert obj.value() == {'a': 1, 'b': 2}
            assert name == 'treevalue_raw'

    def test_treevalue_storage(self):
        st = create_storage({
            'a': 1, 'b': 2, 'c': 'sdklfj',
            'd': {
                'x': [1, 'dfgskjl', None],
                'y': raw({'a': 1, 'b': [2, 3]}),
            }
        })
        with self.transobj_assert(st) as (obj, name):
            assert isinstance(obj, TreeStorage)
            assert obj == st
            assert name == 'treevalue_storage'

    def test_treevalue_tree(self):
        t1 = TreeValue({
            'a': 1, 'b': 2, 'c': 'sdklfj',
            'd': {
                'x': [1, 'dfgskjl', None],
                'y': raw({'a': 1, 'b': [2, 3]}),
            }
        })
        with self.transobj_assert(t1) as (obj, name):
            assert type(obj) == TreeValue
            assert obj == t1
            assert name == 'treevalue_tree'

        t1 = FastTreeValue({
            'a': 1, 'b': 2, 'c': 'sdklfj',
            'd': {
                'x': [1, 'dfgskjl', None],
                'y': raw({'a': 1, 'b': [2, 3]}),
            }
        })
        with self.transobj_assert(t1) as (obj, name):
            assert type(obj) == FastTreeValue
            assert obj == t1
            assert name == 'treevalue_tree'
