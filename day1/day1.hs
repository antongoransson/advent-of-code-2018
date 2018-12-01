import Data.Set (Set)
import qualified Data.Set as Set

main = do 
    input <- readLines "input.txt"
    putStrLn $ "Part 1: " ++ show (solvePart1 input)
    putStrLn $ "Part 2: " ++ show (solvePart2 (cycle input) Set.empty 0)

readLines = fmap (map (toInt . substitute '+' "") .  lines ) . readFile

toInt :: String -> Int
toInt = read

substitute :: Eq a => a -> [a] -> [a] -> [a]
substitute char sub = concatMap replace
  where replace c | c == char = sub
                  | otherwise = [c]

solvePart1 :: [Int] -> Int
solvePart1 = sum

solvePart2 :: [Int] -> Set Int -> Int -> Int
solvePart2 (f:freqs) visitedFreqs current
    | current `Set.member` visitedFreqs = current
    | otherwise = solvePart2 freqs (Set.insert current visitedFreqs) (current + f)
