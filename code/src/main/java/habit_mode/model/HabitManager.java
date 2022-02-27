package habit_mode.model;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

/** 
 * Habit Manager Class.
 * 
 * @author	Team 1
 * @version Spring 2022
 */
public class HabitManager implements List<Habit> {
    private static final String INDEX_IS_EXCLUSIVELY_GREATER_THAN_COLLECTION_SIZE_ERROR = "Cannot get a Habit from index greater or equal to the size of the collection.";
    private static final String INDEX_IS_INCLUSIVELY_GREATER_THAN_COLLECTION_SIZE_ERROR = "Cannot get a Habit from index greater than the size of the collection.";
    private static final String INDEX_LESS_THAN_ZERO_ERROR = "The index cannot be less than 0";
    private static final String FIRST_INDEX_IS_LARGER_ERROR = "the first index cannot be greater than the second index it is trying to reach.";
    private static final String NULL_OBJECT_ERROR = "Object cannot be null";
    private List<Habit> habits;

    /**
     * Creates a new Habit Manager.
     * 
     * @precondition None.
     * @postcondition this.size() == 0;
     */
    public HabitManager() {
        this.habits = new ArrayList<Habit>();
    }

    @Override
    public int size() {
        return this.habits.size();
    }

    @Override
    public boolean isEmpty() {
        return this.habits.isEmpty();
    }

    @Override
    public boolean contains(Object object) {
        this.checkObject(object);
        return this.habits.contains(object);
    }

    @Override
    public Iterator<Habit> iterator() {
        return this.habits.iterator();
    }

    @Override
    public Object[] toArray() {
        return this.habits.toArray();
    }

    @Override
    public <T> T[] toArray(T[] array) {
        return this.habits.toArray(array);
    }

    @Override
    public boolean add(Habit habit) {
        this.checkObject(habit);
        return this.habits.add(habit);
    }

    @Override
    public boolean remove(Object object) {
        this.checkObject(object);
        return this.habits.remove(object);
    }

    @Override
    public boolean containsAll(Collection<?> collection) {
        this.checkObject(collection);
        return this.habits.containsAll(collection);
    }

    @Override
    public boolean addAll(Collection<? extends Habit> collection) {
        this.checkObject(collection);
        return this.habits.addAll(collection);
    }

    @Override
    public boolean addAll(int index, Collection<? extends Habit> collection) {
        this.checkIndexInclusively(index);
        this.checkObject(collection);
        return this.habits.addAll(index, collection);
    }

    @Override
    public boolean removeAll(Collection<?> collection) {
        this.checkObject(collection);
        return this.habits.removeAll(collection);
    }

    @Override
    public boolean retainAll(Collection<?> collection) {
        this.checkObject(collection);
        return this.retainAll(collection);
    }

    @Override
    public void clear() {
        this.habits.clear();
    }

    @Override
    public Habit get(int index) {
        this.checkIndexExclusively(index);
        return this.habits.get(index);
    }

    @Override
    public Habit set(int index, Habit habit) {
        this.checkIndexExclusively(index);
        this.checkObject(habit);
        return this.habits.set(index, habit);
    }

    @Override
    public void add(int index, Habit habit) {
        this.checkIndexInclusively(index);
        this.checkObject(habit);
        this.habits.add(index, habit);
    }

    @Override
    public Habit remove(int index) {
        this.checkIndexExclusively(index);
        return this.habits.remove(index);
    }

    @Override
    public int indexOf(Object object) {
        this.checkObject(object);
        return this.habits.indexOf(object);
    }

    @Override
    public int lastIndexOf(Object object) {
        this.checkObject(object);
        return this.habits.lastIndexOf(object);
    }

    @Override
    public ListIterator<Habit> listIterator() {
        return this.habits.listIterator();
    }

    @Override
    public ListIterator<Habit> listIterator(int index) {
        this.checkIndexInclusively(index);
        return this.habits.listIterator(index);
    }

    @Override
    public List<Habit> subList(int fromIndex, int toIndex) {
        this.checkIndexInclusively(fromIndex);
        this.checkIndexInclusively(toIndex);
        if (fromIndex > toIndex) {
            throw new IllegalArgumentException(FIRST_INDEX_IS_LARGER_ERROR);
        }
        return this.habits.subList(fromIndex, toIndex);
    }

    private void checkObject(Object object) {
        if (object == null) {
            throw new IllegalArgumentException(NULL_OBJECT_ERROR);
        }
    }

    private void checkIndexInclusively(int index) {
        if (index < 0) {
            throw new IllegalArgumentException(INDEX_LESS_THAN_ZERO_ERROR);
        }
        if (index > this.size()) {
            throw new IllegalArgumentException(INDEX_IS_INCLUSIVELY_GREATER_THAN_COLLECTION_SIZE_ERROR);
        }
    }

    private void checkIndexExclusively(int index) {
        if (index < 0) {
            throw new IllegalArgumentException(INDEX_LESS_THAN_ZERO_ERROR);
        }
        if (index >= this.size()) {
            throw new IllegalArgumentException(INDEX_IS_EXCLUSIVELY_GREATER_THAN_COLLECTION_SIZE_ERROR);
        }
    }
}