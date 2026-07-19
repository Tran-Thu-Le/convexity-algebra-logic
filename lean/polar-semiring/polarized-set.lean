import Mathlib.Logic.Function.Basic

variable {X : Type*} (star : X → X)

theorem star_bijective (h : ∀ x, star (star x) = x) :
    Function.Bijective star := by
  constructor
  · -- Injective: nếu star a = star b thì a = b
    intro a b hab
    have := congrArg star hab
    simpa [h] using this
  · -- Surjective: với mọi y, tồn tại x sao cho star x = y
    intro y
    exact ⟨star y, h y⟩
