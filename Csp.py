import copy
from treelib import Tree
from Sudoku import sudoku

class csp_algho:
    def __init__(self,model):
        self.su = sudoku(model=model)
        self.model=model
        self.fc_tree=Tree()
        self.block={0:[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)],
            1:[(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)],
            2:[(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],
            3:[(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)],
            4:[(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)],
            5:[(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],
            6:[(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)],
            7:[(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)],
            8:[(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]
            }

    def forward_checking(self,parent,pmodel):
        i,j=self.su.find_min(pmodel)
        return_value=[]

        if not i=='' and not j=='':
            temp=pmodel[i][j]

            for num in temp[1]:
                model_copy=copy.deepcopy(pmodel)
                item=model_copy[i][j][1].pop(model_copy[i][j][1].index(num))
                model_copy[i][j][0]=item
                model_temp=self.su.find_blocks(blocks=self.block, model=model_copy)

                if self.su.find_error(model_temp):
                    return_value=model_temp
                    hash = self.su.hash(model_copy)
                    self.fc_tree.create_node(hash, hash, parent, model_temp)
                    self.forward_checking(hash,model_temp)
                else:pass

        if self.su.is_end(return_value):
            self.su.printState(return_value)

    def run(self):
        self.su.find_blocks(blocks=self.block, model=self.model)
        hash=self.su.hash(self.model)
        self.fc_tree.create_node('start',hash,None,self.model)
        self.forward_checking(hash,self.model)
