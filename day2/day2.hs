import Data.Set (Set)
import Data.List (groupBy, sort, nub)
import qualified Data.Set as Set

main = do 
    input <- fmap lines $ readFile "input.txt"
    putStrLn $ "Part 1: " ++ show (solvePart1 input)
    putStrLn $ "Part 2: " ++ show (solvePart2 input)

count :: Int -> [[Int]] -> Int
count x = length . concatMap (filter (==x))

solvePart1 :: [String] -> Int
solvePart1 input = count 2 (ids input) * count 3 (ids input)
        where
            ids = map (nub . map length) . (map $ (groupBy (==)) . sort)
solvePart2 input = ""