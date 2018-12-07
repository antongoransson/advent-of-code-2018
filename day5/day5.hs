import Data.Char (toLower, toUpper)

main = do 
    input <- readFile "input.txt"
    putStrLn $ "Part 1: " ++ show (solvePart1 input)
    putStrLn $ "Part 2: " ++ show (solvePart2 input)

alphabet = "abcdefghijklmnopqrstuvwxyz"

reaction :: String -> String -> String
reaction stack [] = stack
reaction [] (x:xs) = reaction [x] xs
reaction (c:stack) (x:xs) 
    | c /= x  && toLower c == toLower x = reaction stack xs
    | otherwise = reaction (x:c:stack) xs

solvePart1 :: String -> Int
solvePart1 = (length . reaction [])

prepareInput:: String -> [String]
prepareInput input = map (const (reaction [] input)) alphabet

solvePart2 :: String -> Int
solvePart2 input = minimum . map length $ [reaction [] (filter ((/=c).toLower) input) | c <- alphabet]