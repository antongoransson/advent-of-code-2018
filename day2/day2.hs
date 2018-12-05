import Data.Set (Set)
import Data.List (groupBy, sort, nub)
import qualified Data.Set as Set

main = do 
    input <- fmap lines $ readFile "input.txt"
    putStrLn $ "Part 1: " ++ show (solvePart1 input)
    putStrLn $ "Part 2: " ++ solvePart2 input

count :: Int -> [[Int]] -> Int
count x = length . concatMap (filter (==x))

solvePart1 :: [String] -> Int
solvePart1 input = count 2 (ids input) * count 3 (ids input)
        where
            ids = map (nub . map length) . (map $ (groupBy (==)) . sort)

solvePart2 :: [String] -> String
solvePart2 = getStr . filter (\p -> diff p == 1) . combinations

combinations :: [a] -> [(a, a)]
combinations [] = []
combinations (x:xs) = map ((,) x) xs ++ combinations xs

getStr :: [(String, String)] -> String
getStr ((p1, p2):xs) = removeWrongChar p1 p2
        where 
            removeWrongChar [] [] = ""
            removeWrongChar (s1:string1) (s2:string2) 
                | s1 == s2 = s1:removeWrongChar string1 string2
                | otherwise = "" ++ removeWrongChar string1 string2

diff :: (String, String) -> Int
diff (s1, s2) = getDiff s1 s2 0
    where 
    getDiff [] [] i = i
    getDiff (c1:s1) (c2:s2) i
        | c1 == c2 = getDiff s1 s2 i
        | otherwise = getDiff s1 s2 (i + 1)