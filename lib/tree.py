class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    return self._get_element_by_id(self.root, id)

  def _get_element_by_id(self, node, id):
    if node.get('id') == id:
      return node


    for child in node.get('children', []):
      result = self._get_element_by_id(child, id)
      if result:
        return result

    return None
