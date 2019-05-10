
class sudoku:

    def __init__(self,model):
        """Initialize model attributs"""
        self.model=model

    def is_end(self,model):
        """ check sudoku is solved or not"""
        end_game=True
        if model:
            for row in model:
                for col in row:
                    if col[0]==0:
                        end_game=False
                        break
        else:
            end_game=False
        return end_game

    def find_blocks_domain(self, block):
        """ find blocks domain"""
        domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for box1 in block:
            if box1[0] in domain:
                domain.remove(box1[0])
        for box2 in block:
            if box2[0]==0:
                for n in domain:
                    if domain:
                        box2[1].append(n)
        return domain


    def find_box_rdomain(self,model):
        """ find boxs domain in row"""
        not_empty_boxs=[]
        for row in model:
            for item1 in row:
                if not item1[0]==0:
                    not_empty_boxs.append(item1[0])

            for item2 in row:
                for number in not_empty_boxs:
                    if number in item2[1]:
                        if item2[1]:
                            item2[1].remove(number)
            not_empty_boxs=[]


    def find_box_cdomain(self,model):
        """ find box domain in column """
        not_empty_box=[]
        for i in range(9):
            for j in range(9):
                item=model[j][i]
                if not item[0]==0:
                    not_empty_box.append(item[0])
            for j in range(9):
                item = model[j][i]
                for number in not_empty_box:
                    if number in item[1]:
                        item[1].remove(number)
            not_empty_box=[]


    def find_blocks(self,blocks,model):
        """return final mode with final domain """
        block=[]
        for num in blocks:
            iblock=blocks[num]
            for j in iblock:
                item=model[j[0]][j[1]]
                item[1]=[]
                block.append(item)
            self.find_blocks_domain(block)
            block=[]
        self.find_box_rdomain(model)
        self.find_box_cdomain(model)

        return model

    def find_min(self,model):
        """ finding minimum domain in model"""
        min=9
        r_index=''
        c_index=''
        for row in model:
            for item in row:
                if item[0]==0:
                    if len(item[1])<min:
                        min=len(item[1])
                        r_index=model.index(row)
                        c_index=row.index(item)

        return r_index,c_index


    def find_error(self,model):
        """ predict empty domain"""
        for row in model:
            for item in row:
                if item[0]==0 and len(item[1])==0:
                    return False
        return True

    def printState(self,model):
        """ print sudoku model"""
        m=0
        for i in model:
            if not m % 3:
                print('====================================')
            print(str(i[0][0])+' : '+str(i[1][0])+' : '+str(i[2][0])+' || '+str(i[3][0])+' : '+str(i[4][0])+' : '+str(i[5][0])
                  +' || '+str(i[6][0])+' : '+str(i[7][0])+' : '+str(i[8][0]))
            m+=1
        print('====================================')
