import Data.Set (Set)
import qualified Data.Set as Set

main = do 
    input <- fmap (map parse . lines) $ readFile "input.txt"
    putStrLn $ "Part 1: " ++ show (solvePart1 input)
    putStrLn $ "Part 2: " ++ show (solvePart2 input)

parse :: String -> Int
parse = read . filter (/= '+')

solvePart1 :: [Int] -> Int
solvePart1 = sum

solvePart2 ::  [Int] -> Int
solvePart2 = solve Set.empty 0 . cycle 
    where solve visitedFreqs current (f:freqs) 
                | current `Set.member` visitedFreqs = current
                | otherwise = solve (Set.insert current visitedFreqs) (current + f) freqs
