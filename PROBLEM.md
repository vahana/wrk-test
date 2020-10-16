# Wrk Coding Interview

## Phase 1

Add an animal - a deer, wandering around.

* Has a hunger value.
* Able to look around in the immediate vicinity.
  * If the hunger value is below a threshold, looks for trees to eat.
  * Otherwise, looks for another deer to mate with. Hungry deer don't mate.
  * Otherwise wanders randomly.
* When it eats a tree:
  * The tree is removed from the world.
  * The hunger value is increased by a set value.
* When it mates with another deer, has a random chance of spawning another deer in an adjacent space.
* If it doesn't eat for a certain amount of time, dies.

## Phase 2

Add a mountain lion:

* Same process as a deer, but looks for deer instead of trees.
* Mountain lions do not eat trees, so the cannot attempt to move into a space with a tree.

Update the deer to run away from mountain lions.
