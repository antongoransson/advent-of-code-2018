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
solvePart2 = solve Set.empty . scanl (+) 0 . cycle 
    where solve visitedFreqs (f:freqs) 
                | f `Set.member` visitedFreqs = f
                | otherwise = solve (Set.insert f visitedFreqs) freqs
