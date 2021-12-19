module Main where 


{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE ExtendedDefaultRules #-}
{-# LANGUAGE ScopedTypeVariables #-}
{-# OPTIONS_GHC -fno-warn-type-defaults #-}


import Shelly hiding (FilePath)
import qualified Data.Text as T
import qualified Filesystem.Path as F
import System.IO 
import System.Console.GetOpt
import qualified Data.Map as M
import System.Environment (getArgs) 
import Control.Monad.Trans
import Control.Monad.Reader.Class
import Control.Monad.Reader
import Control.Applicative
import Data.List hiding (all)
import Text.Printf
import Data.Ord
import System.FilePath 
import System.Exit
import Control.Exception.Base
import Text.Printf


main = 
  do
    (f, a) <- parseArgs
    putStrLn $ "GotArgs: " ++ (f) ++ (" ") ++ (show a)
    shelly . (verbosely) . (escaping False) $ testSolver (f, a)

{- Mainfunction to run, fetches test instances and runs them -}

testSolver :: (FilePath, [T.Text]) -> Sh () 
testSolver (s, a) = 
  do
    allInstaces <-  sort . map (snd . T.breakOnEnd (T.singleton '/'))  <$> lsT baseFolder
   -- echo . T.pack $ "ALL INSTANCES: " 
   -- echo_n . T.unlines $ allInstaces
    let 
      testI = filter toBeTested allInstaces
    --echo . T.pack $ "TEST INSTANCES: " 
    --echo_n . T.unlines $ testI
    mapM (checkInstance (s, a)) testI >>= echo_err . T.pack . ("Total Time: "++)  . (\t -> printf "%.5f" t) . sum



checkInstance :: (FilePath, [T.Text]) -> T.Text -> Sh (Double)
checkInstance d i = 
  do
    (t,  cost) <- time (runOneInstance d i)
    let
      realC = instCost M.! i
      endStr =  T.pack $  if cost == realC then "OK" else "<<<<<<<< PROBLEM"
      outP = T.unwords [T.pack "####INSTANCE: ", i, T.pack $ "Real " ++ (show realC), T.pack $ "Observed " ++ (show cost), 
                        T.pack ("Time " ++ (printf "%.5f" t))  , endStr]
    echo outP
    echo_err outP
    return t

runOneInstance :: (FilePath, [T.Text]) -> T.Text -> Sh (Int)
runOneInstance  (solver, args) i = errExit False $
  do
    findOpt <$> run (s2fP ("./" ++ solver)) (args ++ [(wholeI i)]) 
  where
    findOpt = read . T.unpack . last . T.words . last . filter ((== 'o')  . T.head) . filter (not . T.null) . T.lines 



s2fP = fromText . T.pack
baseFolder = s2fP "TestInstances"



wholeI i =  T.append (T.pack "TestInstances/") i

toBeTested f = f `elem` (M.keys instCost) 

----------------------------ARGUMENT HANDLING----------------------------------------------
data Options = Options { 
                        solverName :: FilePath,
                        args :: [T.Text]
                       }

deafultInst  = Options {     
                        solverName = "loandra" ,
                        args = [T.pack "-algorithm=1"]
                       }


options :: [OptDescr (Options -> Options)]
options = [
    Option ['s'] ["Solver"] (ReqArg (\x opts -> opts { solverName = x }) "File") "Name of Solver to Test, defaults to open-wbo",
    Option ['a'] ["args"]   (ReqArg (\x opts -> opts { args = (T.splitOn (T.singleton ',')) . T.pack $ x }) "Arguments")  "Arguments to use (, separated)"
          ]

header = "Usage: main [OPTION...]"

parseArgs :: IO (FilePath, [T.Text])
parseArgs = 
  do
   argv <- getArgs
   let (o, nonreq, errors) = getOpt RequireOrder options argv
   if ((not . null) nonreq || (not. null) errors || (null o))
      then (putStrLn $ (usageInfo header options) ++ ((concat nonreq) ++ (concat errors))) >> exitFailure
      else return ()
   let
       opts = foldl (flip id) deafultInst o
   return (solverName opts, args opts) 

instCost :: M.Map T.Text Int
instCost = 
  M.fromList [
    (T.pack "ped2.G.recomb10-0.01-4.wcnf", 58784),
    (T.pack "ped2.G.recomb10-0.20-11.wcnf", 50061),
    (T.pack "ped2.G.recomb1-0.20-11.wcnf", 4103),
    (T.pack "103c9978-5408-11df-9bc1-00163e7a6f5e_l1.wcnf", 3795246),
    (T.pack "1502.wcsp.log.wcnf", 28042),
    (T.pack "4a69cf16-c731-11df-9182-00163e3d3b7c_l1.wcnf", 186592),
    (T.pack "503.wcsp.log.wcnf", 11113),
    (T.pack "54.wcsp.dir.wcnf", 37),
    (T.pack "8.wcsp.dir.wcnf", 2),
    (T.pack "ab9005be-bacc-11e0-b0f6-00163e1e087d_l1.wcnf", 84964),
    (T.pack "bwt7.wcsp.wcnf", 780),    
    (T.pack "CSG140-140-46.wcnf", 16960),
    (T.pack "driverlog04ac.wcsp.wcnf", 1790),
    (T.pack "driverlog04bc.wcsp.wcnf", 1921),
    (T.pack "driverlog04cc.wcsp.wcnf", 2932),
    (T.pack "mancoosi-test-i1000d0u98-18.wcnf", 152228825),
    (T.pack "mprime04cc.wcsp.wcnf",931),
    (T.pack "mprime04c.wcsp.wcnf", 590),
    (T.pack "ped2.B.recomb1-0.10-7.wcnf", 588),
    (T.pack "ped3.D.recomb10-0.20-12.wcnf", 349),
    (T.pack "rand307_l2.wcnf", 1820365),
    (T.pack "random-net-50-2_network-2.net.wcnf", 43675),
    (T.pack "WCNF_pathways_p18.wcnf", 228),
    (T.pack "zenotravel04bc.wcsp.wcnf", 4110),
    (T.pack "ped3.G.recomb10-0.20-14.wcnf", 11990),
    (T.pack "1aabfc32-d491-11df-9a24-00163e3d3b7c_l2.wcnf", 8272324),
    (T.pack "8680dd8a-8600-11e0-b285-00163e1e087d_l2.wcnf", 8289698),
    (T.pack "mancoosi-test-i4000d0u98-97.wcnf", 903703891),
    (T.pack "ped3.F.recomb10-0.01-5.wcnf", 7540),
    (T.pack "rand981_l2.wcnf", 1878056),
    (T.pack "satellite02bc.wcsp.wcnf", 2289),
    (T.pack "WCNF_pathways_p07.wcnf", 115),
    (T.pack "WCNF_storage_p05.wcnf", 107)
  ]
