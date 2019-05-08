import qualified Data.Map.Strict as Map

type Accounts = Map.Map String Integer
increaseBalance :: String -> Integer -> Accounts -> Accounts
increaseBalance k v state =
    case Map.lookup k state of
    Nothing -> Map.insert k v state
    Just v' -> Map.insert k (v + v') state

data Transaction = Transaction { from :: String, to :: String, amount :: Integer } deriving Show

transactions =
    [
        Transaction { from="Alice", to="Bob", amount=10 },
        Transaction { from="Bob", to="Charlie", amount=5 }
    ]
initialAccounts = Map.empty

processTransaction (Transaction {from=from, to=to, amount=amount}) accounts = let
    accounts' = increaseBalance from (-amount) accounts
    accounts'' = increaseBalance to amount accounts' in
    accounts''

processTransactions [] accounts = accounts
processTransactions (t:ts) accounts = processTransactions ts (processTransaction t accounts)

resultAccounts = processTransactions transactions initialAccounts
