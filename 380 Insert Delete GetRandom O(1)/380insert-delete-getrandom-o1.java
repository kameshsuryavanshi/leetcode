class RandomizedSet {

    private ArrayList<Integer>element;
    private HashMap<Integer,Integer> elementToIndex;
    private Random random;

    public RandomizedSet() {
        element = new ArrayList<>();
        elementToIndex = new HashMap<>();
        random = new Random()   ;
    }
    
    public boolean insert(int val) {
        if(elementToIndex.containsKey(val)){
            return false ;// if already present
        }
        element.add(val);
        elementToIndex.put(val,element.size()-1);
        return true;
    }
    public boolean remove(int val){
        if(!elementToIndex.containsKey(val)){
            return false; // if not present
        }
        int index =  elementToIndex.get(val);
        int lastI = element.size()-1;
        int lastE = element.get(lastI);

        element.set(index,lastE);
        elementToIndex.put(lastE,index);

        element.remove(lastI);
        elementToIndex.remove(val);
        return true;
    }
    public int getRandom() {
        int randomIndex = random.nextInt(element.size());
        return element.get(randomIndex);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */