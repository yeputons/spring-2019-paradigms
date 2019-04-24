import qualified Data.Map.Strict as Map
import Control.Arrow

type Accounts = Map.Map String Int
increaseBalance k v state = Map.insertWith (+) k v state

data Transaction = Transaction { from :: String, to :: String, amount :: Int }

transactions =
    [
        Transaction { from="Alice", to="Bob", amount=10 },
        Transaction { from="Bob", to="Charlie", amount=5 }
    ]
initialAccounts = Map.empty

processTransaction (Transaction {from=from, to=to, amount=amount}) =
    increaseBalance from (-amount) >>> increaseBalance to amount

processTransactions ts accounts = foldr processTransaction accounts ts

resultAccounts = processTransactions transactions initialAccounts
