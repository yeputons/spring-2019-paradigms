import Test.Hspec  -- cabal install hspec
                   -- apt-get install haskell-hspec
main = hspec $ do
  describe "length function" $ do
    it "works on empty list" $ do
      (length []) `shouldBe` 0
    it "works on single-item list" $ do
      (length [10]) `shouldBe` 1
      (length ["foo"]) `shouldBe` 1
