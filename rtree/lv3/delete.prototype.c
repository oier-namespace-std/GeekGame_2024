void delete_node(void) {
  int key;
  struct node *p, *q;
  int *k = &key;
  printf("please enter the key of the node you want to remove\n");
  scanf("%d", k);
  p = root;
  while (p != NULL && p->key != *k) {
    if (p->key > *k)
      p = p->lchild;
    else
      p = p->rchild;
  }
  if (p != NULL) {
    if (p->rchild == NULL) {
      if (p->lchild == NULL) {
        if (p->parent == NULL)
          root = NULL;
        else {
          if (p->parent->lchild == p)
            p->parent->lchild = NULL;
          else
            p->parent->rchild = NULL;
        }
      } else {
        if (p->parent == NULL) {
          root = p->lchild;
        } else {
          if (p->parent->lchild == p)
            p->parent->lchild = p->lchild;
          else
            p->parent->rchild = p->lchild;
        }
      }
    } else {
      if (p->rchild->lchild == NULL) {
        // vuln p->parent->
        q = p->rchild;
        q->lchild = p->lchild;
        q->rchild = p->rchild;
        q->parent = p->parent;
        free(p->data);
        free(p);
      } else {
        q = p->rchild->lchild;
        while (q->rchild != NULL) q = q->rchild;
        p->key = q->key;
        char *temp = p->data;
        p->data = q->data;
        p->rchild = q->rchild;
        if (q->parent->lchild == q)
          q->parent->lchild = q->rchild;
        else
          q->parent->rchild = q->rchild;
        free(temp);
        free(q);
      }
    }
  } else {
    printf("oops! the key is not found\n");
  }
}
